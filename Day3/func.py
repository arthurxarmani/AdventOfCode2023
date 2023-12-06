import numpy as np

def sum_arr(arr):
    """
    Sums the elements in an array
    """
    sum = 0

    for i in arr:
        sum += int(i)

    return sum

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

def get_neighbors(arr, row, col, radius):
    """
    Returns the neighbors of the element at (i, j) in the array as a 2D matrix.
    Has a horizontal radius. (We can only get numbers that are in a row)
    """
    return [[arr[row][col] if row >=0 and row < len(arr) and col >=0 and col < len(arr[0]) else '.'
             for col in range (col-radius, col+1+radius)]
                for row in range(row-1, row+2)]

def check_neighbors(neighbors):
    """
    Returns True if any of the neighbors are symbols, False otherwise.
    """
    for row in neighbors:
        for col in row:
            if is_symbol(col):
                return True
    return False

def build_two_dimensional_array(input_file):
    """
    Builds a two dimensional array from the input file.
    Each character of the input file is an element in the array.
    Each line is a row in the array.
    """
    two_dimensional_array = []
    lines = input_file.readlines()
    for line in lines:
        line = line.strip()
        two_dimensional_array.append([*line])

    return two_dimensional_array


def is_symbol(var):
    """
    Returns True if var is a symbol, False otherwise.
    Symbol in this context is anything not "." or digit.
    """
    if var == '':
        return False
    elif var == '.':
        return False
    elif var.isnumeric():
        return False
    else:
        return True
    
def extract_part_numbers(array, max_len):
    """
    Extracts the part numbers from the array.
    Valid part numbers have a symbol neighbor that is not a "."
    The neighboring symbol can be diagonally located as well.
    The entire part number must be contiguous.
    The symbol can be by any individual digit making up the part number.
    Expects a 2D array.
    """
    part_numbers = []
    current_number = ""
    found_symbol_neighbor = False
    for row in range(len(array)):
        current_number = "" # Reset the current number for each row.
        for col in range(len(array[row])):
            if not array[row][col].isnumeric():
                # We have hit a non-numeric character, so we need to check if we have a valid number.
                if not current_number == "" and found_symbol_neighbor:
                    part_numbers.append(int(current_number))
                    current_number = ""
                    found_symbol_neighbor = False
                else: 
                    current_number = ""
                    found_symbol_neighbor = False

            if array[row][col].isnumeric() and len(current_number) < max_len:
                # We have hit a number, so we check it's neighbors to see if any are symbols.
                current_number += str(array[row][col])
                if not found_symbol_neighbor:
                    neighbors = get_neighbors(array, row, col, 1)
                    found_symbol_neighbor = check_neighbors(neighbors)

            if len(current_number) == max_len:
                # We have reached max length
                if found_symbol_neighbor:
                    part_numbers.append(current_number)
                    current_number = ""
                    found_symbol_neighbor = False
                else: 
                    current_number = ""
                    found_symbol_neighbor = False

    return part_numbers

def print_2d(array):
    """
    Prints a 2D array.
    """
    for row in array:
        print(*row)
    print("\n")


def count_numbers_in_array(array):
    count_numbers = 0
    for row in array:
        for col in row:
            if col.isnumeric():
                count_numbers += 1
    return count_numbers

def replace_all_other_symbols(array):
    """
    Replaces all symbols that are not "*" with "."
    """
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col] == "*":
                if row == 1 and col == 3:
                    continue
                else:
                    array[row][col] = "."
            if not array[row][col].isnumeric():
                array[row][col] = "."
    return array


def extract_gear_ratios(array):
    """
    Extracts the gear ratios from the provided 2D array.
    """
    # Convert the regular array to one that numpy can use.
    numpy_2d_array = np.array(array)

    # numpy will provide the indices where the "*" is located.
    ## A "*" represents a ~possible~ gear ratio.
    indices = np.argwhere(numpy_2d_array == "*")

    gear_ratios = []

    # Iterate through the indices of *'s and check their neighbors.
    for coordinate_pair in indices:
        # Only fetch the full 3 radius neighbors for the neighbor sets that have between 2 and 4 numbers.
        star_neighbors = get_neighbors(array, coordinate_pair[0], coordinate_pair[1], 1)
        count_in_array = count_numbers_in_array(star_neighbors)
        if count_in_array < 2 or count_in_array > 6  :
            continue
        else: 
            # Extract the full 3 radius neighbors (to get the full part number)
            full_neighbors = get_neighbors(array, coordinate_pair[0], coordinate_pair[1], 3)
            full_neighbors = replace_all_other_symbols(full_neighbors)

            part_numbers = extract_part_numbers(full_neighbors, 3)
            if len(part_numbers) == 2:
                gear_ratio = int(part_numbers[0]) * int(part_numbers[1])
                gear_ratios.append(gear_ratio)

    return gear_ratios


