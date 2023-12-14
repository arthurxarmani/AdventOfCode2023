import sys
import numpy as np

def build_initial_universe():
    print('Building the initial universe...')
    initial_universe = []

    input_file = open(sys.argv[1], 'r')
    for line in input_file.readlines():
        initial_universe.append(list(line.strip()))
    return np.array(initial_universe)

def expand_the_universe(initial_universe, times_larger):
    print('Expanding the universe...')
    expanded_universe = np.copy(initial_universe)
    char_to_search = "#"

    # First process the rows
    empty_row = np.array(['.'] * expanded_universe.shape[1])
    # Multiply number of empty_rows by times_larger
    empty_rows = np.array([empty_row] * times_larger)

    # Search for the character in each row
    insert_after_row_indices = []
    for row_index, row in enumerate(initial_universe):
        if not char_to_search in row:
            insert_after_row_indices.append(row_index)

    for insert_after_row_index in reversed(insert_after_row_indices):
        upper_part = expanded_universe[:insert_after_row_index + 1]
        lower_part = expanded_universe[insert_after_row_index + 1:]
        array = np.vstack([upper_part, empty_rows, lower_part])
        expanded_universe = array

    # Then process the columns
    # Multiply the number of empty columns by times_larger
    empty_col = np.array([['.']] * expanded_universe.shape[0])
    empty_cols = np.repeat(empty_col, times_larger, axis=1)

    # Search for the character in each row
    insert_after_col_indices = []
    for idx in range(expanded_universe.shape[1]):
        if not char_to_search in expanded_universe[:,idx]:
            insert_after_col_indices.append(idx)

    for insert_after_col_idx in reversed(insert_after_col_indices):
        left_part = expanded_universe[:, :insert_after_col_idx + 1]
        right_part = expanded_universe[:, insert_after_col_idx + 1:]
        array = np.hstack([left_part, empty_cols, right_part])
        expanded_universe = array

    return expanded_universe

def number_the_universe(universe):
    print('Numbering the universe...')

    # With numpy, we need to have the right datatype for the array.
    # Calculating the max number length will help us determine the right datatype.
    max_num_length = len(str(np.prod(universe.shape))) # max_num_length = string length of (num_rows x num_cols)
    
    # Create a new array with a suitable datatype
    numbered_universe = np.empty(universe.shape, dtype=f'U{max_num_length}')

    # Initialize numbered_universe with the elements from universe
    for i in range(universe.shape[0]):
        for j in range(universe.shape[1]):
            numbered_universe[i, j] = universe[i, j]

    current_number = 1
    for row in range(numbered_universe.shape[0]):
        for col in range(numbered_universe.shape[1]):
            if numbered_universe[row, col] == '#':
                numbered_universe[row, col] = str(current_number)
                current_number += 1
    return numbered_universe

def print_the_universe(universe):
    print('Printing the universe...')
    for row in universe:
        print(*row)
    print('\n')

def generate_coordinates(numbered_universe):
    print('Generating coordinate map...')
    coords = {}
    for row in range(numbered_universe.shape[0]):
        for col in range(numbered_universe.shape[1]):
            # We expect numbers
            if numbered_universe[row, col].isnumeric():
                coords[int(numbered_universe[row, col])] = (row, col)
    return coords

def calculate_shortest_path(coords, galaxy_num_1, galaxy_num_2):
    galaxy_1_coords = coords[galaxy_num_1]
    galaxy_2_coords = coords[galaxy_num_2]
    shortest_path = abs(galaxy_1_coords[0] - galaxy_2_coords[0]) + abs(galaxy_1_coords[1] - galaxy_2_coords[1])
    return shortest_path

def fetch_sum_of_shortest_paths(coords):
    print('Fetching sum of shortest paths...')
    sum = 0
    # We need to pair up each galaxy with every other galaxy, while ensuring no duplicates.
    # 1 pairs with 2
    # 1 pairs with 3
    # 1 pairs with 4
    # 2 pairs with 3
    # 2 pairs with 4
    # 3 pairs with 4
    galaxy_numbers = list(coords.keys())
    for i in range(len(galaxy_numbers)):
        for j in range(i + 1, len(galaxy_numbers)):
            sum += calculate_shortest_path(coords, galaxy_numbers[i], galaxy_numbers[j])

    return sum

def calculate_result_of_x_expansions(expansions, initial_universe):
    expanded_universe_1 = expand_the_universe(initial_universe, 1)
    numbered_universe_1 = number_the_universe(expanded_universe_1)
    coords_1 = generate_coordinates(numbered_universe_1)

    res_expansion_1 = fetch_sum_of_shortest_paths(coords_1)

    expanded_universe_2 = expand_the_universe(initial_universe, 2)
    numbered_universe_2 = number_the_universe(expanded_universe_2)
    coords_2 = generate_coordinates(numbered_universe_2)

    res_expansion_2 = fetch_sum_of_shortest_paths(coords_2)

    difference_between_expansions = res_expansion_2 - res_expansion_1

    return res_expansion_1 + (difference_between_expansions * (expansions - 1))


initial_universe = build_initial_universe()
print('Initial universe:')
print_the_universe(initial_universe)
print(initial_universe.shape)

# Looking for a pattern by finding the results for different expansions on the example...
expanded_universe = expand_the_universe(initial_universe, 1)            # 374
#expanded_universe = expand_the_universe(initial_universe, 2)            # 456 (+82)
#expanded_universe = expand_the_universe(initial_universe, 3)            # 538 (+82)
#expanded_universe = expand_the_universe(initial_universe, 4)            # 620 (+82)
#expanded_universe = expand_the_universe(initial_universe, 5)            # 702 (+82)
#expanded_universe = expand_the_universe(initial_universe, 6)            # 784 (+82)
#expanded_universe = expand_the_universe(initial_universe, 7)            # 866 (+82)
# ...
#expanded_universe = expand_the_universe(initial_universe, 10 - 1)       # 1030 


print('Expanded universe:')
print_the_universe(expanded_universe)
print(expanded_universe.shape)

numbered_universe = number_the_universe(expanded_universe)
print('Numbered universe:')
print_the_universe(numbered_universe)

coords = generate_coordinates(numbered_universe)
print('Coordinate map:')
print(coords)

# Examples - python app.py example
# Actual - python app.py input

# print('Shortest path between 1 and 7:')
# print(calculate_shortest_path(coords, 1, 7))

# print('Shortest path between 3 and 6:')
# print(calculate_shortest_path(coords, 3, 6))

# print('Shortest path between 8 and 9:')
# print(calculate_shortest_path(coords, 8, 9))

sum_of_shortest_paths = fetch_sum_of_shortest_paths(coords)
print(sum_of_shortest_paths)
# Answer for part 1 is 9214785.

# Part 2
print(calculate_result_of_x_expansions(1000000-1, initial_universe))
# Answer for part 2 is 613686987427.

