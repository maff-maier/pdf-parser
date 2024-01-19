import pdfplumber
import regex
import json
import argparse

from typing import List
from classes import *


def get_filename() -> str:
    parser = argparse.ArgumentParser()

    parser.add_argument('filename', type=str)
    args = parser.parse_args()

    return args.filename


def parse(file_name: str) -> None:
    full_info = ChampInfo()

    filtered_list = parse_pdf(file_name=file_name, full_info=full_info)

    assemble_info(filtered_list=filtered_list, full_info=full_info)

    age_range_filter(full_info=full_info)

    to_json(file_name=file_name, full_info=full_info)


def assemble_info(filtered_list: List[str], full_info: ChampInfo) -> None:
    for ind in range(len(filtered_list)):
        if (ages := regex.header.search(filtered_list[ind])) is not None:
            age = Ages()
            age.range_name = ages.string.strip()
            age.ages = []
            ind += 1

            while ind < len(filtered_list) and (name := regex.names.search(filtered_list[ind])) is not None:
                person = Person()

                person.initials = name.string.strip()
                person.distanses = []

                ind += 1

                while ind < len(filtered_list) and len(distance := regex.dist_time.findall(filtered_list[ind])):
                    for mtch in distance:
                        new_dist = DistanseTime()

                        new_dist.distance = mtch[0]
                        new_dist.sum_time = mtch[1]
                        new_dist.time = mtch[2]

                        person.distanses.append(new_dist)
                    ind += 1

                age.ages.append(person)

            full_info.participants.append(age)


def parse_pdf(file_name: str, full_info: ChampInfo) -> List[str]:
    filter_list = []

    with pdfplumber.open(file_name) as pdf:

        page = pdf.pages[0]

        text = page.extract_text()
        distnt = regex.dist.findall(text)

        full_info.sex = 'M' if 'Мальчики' in text else 'F'
        full_info.champ_type = 'Final' if 'Финальный' in text else 'Prepatory'
        full_info.distance = distnt[0]
        full_info.participants = []

        for page in pdf.pages:
            text = page.extract_text()

            text = text.split('\n')

            for line_index in range(len(text)):
                mnames = regex.names.search(text[line_index])

                mheader = regex.header.search(text[line_index])

                if mnames is not None:
                    filter_list.append(mnames.group(2))
                    line_index += 1

                    while len(regex.dist.findall(text[line_index])):
                        filter_list.append(text[line_index])
                        line_index += 1

                elif mheader is not None:
                    filter_list.append(mheader.group(1))
    return filter_list


def age_range_filter(full_info: ChampInfo) -> None:
    left = 0
    right = 1

    while left < len(full_info.participants) and right < len(full_info.participants):
        if full_info.participants[left].range_name == full_info.participants[right].range_name:
            full_info.participants[left].ages.extend(
                full_info.participants[right].ages)
            full_info.participants.pop(right)
        else:
            left = right
            right += 1


def to_json(file_name: str, full_info: ChampInfo) -> None:
    json_info = json.dumps(full_info, cls=Encoder, ensure_ascii=False)
    name = file_name.split('.')[0] + '.json'

    with open(name, 'w') as f:
        f.write(json_info)
