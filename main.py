def main():
    strings_from_1_file = get_data_from_file("source_file_1.txt")
    strings_from_2_file = get_data_from_file("source_file_2.txt")
    same_strings = get_same_strings(strings_from_1_file, strings_from_2_file)
    put_data_to_file(strings_from_1_file, same_strings, "result_file_1.txt")
    put_data_to_file(strings_from_2_file, same_strings, "result_file_2.txt")


def get_data_from_file(file_name):
    result = []
    with open(file_name, encoding='ascii') as source_file:
        for line in source_file:
            result.append(line.strip())
    return result


def get_same_strings(strings_from_1_file, strings_from_2_file):
    result = set()
    for string_1 in strings_from_1_file:
        for string_2 in strings_from_2_file:
            if string_1 == string_2:
                result.add(string_1)
                break
            if string_1 < string_2:
                break
    return result


def put_data_to_file(strings_from_file, same_strings, result_file_name):
    with open(result_file_name, 'w', encoding='ascii') as result_file:
        for string in strings_from_file:
            if string not in same_strings:
                result_file.write(string + "\n")


if __name__ == '__main__':
    main()
