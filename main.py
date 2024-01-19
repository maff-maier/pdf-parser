from parse import parse, get_filename


def main() -> None:
    file_name = get_filename()

    parse(file_name=file_name)


if __name__ == '__main__':
    main()
