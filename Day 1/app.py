import sys
from func import extract_num_input
from func import sum_arr

"""
Open the file specified by the first argument.
Extract first and last numbers from each line in the file.
Sum the result.
"""
input_file = open(sys.argv[1], 'r')
numbers = extract_num_input(input_file)
input_file.close()

print("sum: " + str(sum_arr(numbers)))
