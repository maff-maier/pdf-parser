import pdfplumber
import regex
import json

from io import BytesIO
from fastapi import HTTPException
from typing import List
from classes import *
from utils import distance_validation, min_to_sec_convert


def parse(file: BytesIO) -> str:
    full_info = ChampInfo()

    filtered_list = parse_pdf(file=file, full_info=full_info)

    assemble_info(filtered_list=filtered_list, full_info=full_info)

    min_to_sec_convert(full_info=full_info)

    if not distance_validation(info=full_info):
        raise HTTPException(status_code=422, detail={
                            "error": "Wrong max distance in file"})

    if not len(full_info.swimmers) or not len(full_info.distance):
        raise HTTPException(status_code=422, detail={
                            "error": "No info in result. Check file validity."})

    return to_json(full_info=full_info)


def parse_pdf(file: str, full_info: ChampInfo) -> List[str]:
    filter_list = []
    with pdfplumber.open(file) as pdf:

        page = pdf.pages[0]

        text = page.extract_text()
        distnt = regex.dist.findall(text)

        full_info.distance = distnt[0]

        for page in pdf.pages:
            text = page.extract_text().split('\n')

            for line_index in range(len(text)):
                mnames = regex.names.search(text[line_index])
                if mnames is not None:
                    filter_list.append(mnames.group(2))

                    if full_info.distance == '50m':
                        dist_time = regex.dist_50.findall(text[line_index])[0]
                        filter_list.append(dist_time)
                        continue

                    line_index += 1
                    while len(regex.dist.findall(text[line_index])):
                        filter_list.append(text[line_index])
                        line_index += 1
    return filter_list


def assemble_info(filtered_list: List[str], full_info: ChampInfo) -> None:
    if full_info.distance == '50m':
        skip_50m_next_line_flag = False
        for ind, line in enumerate(filtered_list):
            if skip_50m_next_line_flag:
                skip_50m_next_line_flag = False
                continue

            person = Person()
            person.initials = line

            distance = DistanceTime()

            distance.distance = '50m'
            distance.time = filtered_list[ind + 1]
            distance.total = filtered_list[ind + 1]

            person.distances.append(distance)
            full_info.swimmers.append(person)

            skip_50m_next_line_flag = True
    else:
        ind = 0
        while ind < len(filtered_list):
            person = Person()
            person.initials = filtered_list[ind]
            ind += 1

            while ind < len(filtered_list) and len(distance := regex.dist_time.findall(filtered_list[ind])):
                for mtch in distance:
                    new_dist = DistanceTime()

                    new_dist.distance = mtch[0]
                    new_dist.total = mtch[1]
                    new_dist.time = mtch[2]

                    person.distances.append(new_dist)

                ind += 1

            full_info.swimmers.append(person)


def to_json(full_info: ChampInfo) -> str:
    return json.dumps(full_info, cls=Encoder, ensure_ascii=False)
