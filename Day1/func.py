import regex as re


def sum_arr(arr):
    """
    Sums the elements in an array
    """
    sum = 0

    for i in arr:
        sum += i

    return sum


def convert_to_digit(word):
    """
    Converts a word to a digit
    """
    switcher = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    return switcher.get(word, "Invalid number")


def extract_num_input(input_file):
    """
    Extracts numbers into an array from the input file
    Input file is a text file with numbers separated by letters.

    1abc2               -> 12
    pqr3stu8vwx         -> 38
    a1b2c3d4e5f         -> 15
    treb7uchet          -> 77
    two1nine            -> 29
    eightwothree        -> 83
    abcone2threexyz     -> 13
    xtwone3four         -> 24
    4nineeightseven2    -> 42
    zoneight234         -> 14
    7pqrstsixteen       -> 76

    We want the first and last number in each line.
    """
    numbers = []
    lines = input_file.readlines()

    for line in lines:
        extracted_number = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)

        if len(extracted_number) > 0:
            first_number = extracted_number[0]
            last_number = extracted_number[-1]
            if not first_number.isdigit():
                first_number = convert_to_digit(first_number)
            if not last_number.isdigit():
                last_number = convert_to_digit(last_number)
            stringified_number = first_number + last_number
            numbers.append(int(stringified_number))

    return numbers
