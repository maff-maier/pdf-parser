import regex
from classes import *
from parse import parse


def main():
    full_info = ChampInfo()
    file_name = 'ResultList_103F.pdf'

    parse(file_name=file_name, full_info=full_info)


if __name__ == '__main__':
    main()
