import regex as re

def is_equal_array(arr1, arr2):
    """
    Returns True if the two arrays are equal, False otherwise.
    """
    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    
    return True

def get_winning_numbers(line):
    """
    A line looks like 
    Card   1: 33 56 23 64 92 86 94  7 59 13 | 86 92 64 43 10 70 16 55 79 33 56  8  7 25 82 14 31 96 94 13 99 29 69 75 23
    """
    stripped_line = line.split(": ")[1] # This will get us the part after the card number.
    stripped_line = stripped_line.split(" | ")[0] # This will get us the part before the "your_numbers" section.
    stripped_line = stripped_line.split()
    winning_numbers = []
    for number in stripped_line:
        number = int(number)
        winning_numbers.append(number)

    return winning_numbers

def get_your_numbers(line):
    """
    A line looks like 
    Card   1: 33 56 23 64 92 86 94  7 59 13 | 86 92 64 43 10 70 16 55 79 33 56  8  7 25 82 14 31 96 94 13 99 29 69 75 23
    """
    stripped_line = line.split(" | ")[1]
    stripped_line = stripped_line.split()
    your_numbers = []
    for number in stripped_line:
        number = int(number)
        your_numbers.append(number)
        
    return your_numbers
