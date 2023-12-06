import func
import sys
from func import extract_part_numbers, extract_gear_ratios, sum_arr

input_file = open(sys.argv[1], 'r')
array = func.build_two_dimensional_array(input_file)

MAX_PART_LENGTH = 3

part_numbers = extract_part_numbers(array, MAX_PART_LENGTH)

print("sum of part numbers: " + str(sum_arr(part_numbers)))

gear_ratios = extract_gear_ratios(array)
print("sum of gear ratios: " + str(sum_arr(gear_ratios)))
