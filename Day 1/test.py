import io
from func import extract_num_input
from func import sum_arr

# Test case 1: Single line with numbers
input_file_1 = io.StringIO("1abc2\n")
expected_output_1 = [12]
assert extract_num_input(input_file_1) == expected_output_1

# Test case 2: Multiple lines with numbers
input_file_2 = io.StringIO("1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet\n")
expected_output_2 = [12, 38, 15, 77]
assert extract_num_input(input_file_2) == expected_output_2

# Test case 3: Empty input file
input_file_3 = io.StringIO("")
expected_output_3 = []
assert extract_num_input(input_file_3) == expected_output_3

# Test case 4: No numbers in input file
input_file_4 = io.StringIO("abc\ndef\n")
expected_output_4 = []
assert extract_num_input(input_file_4) == expected_output_4

# Test case 5: Numbers with leading and trailing characters
input_file_5 = io.StringIO("a1b2c3d4e5f\n")
expected_output_5 = [15]
assert extract_num_input(input_file_5) == expected_output_5

print("All test cases for part 1 of extraction passed!")


# Test case 1: Empty array
arr1 = []
expected1 = 0
assert sum_arr(arr1) == expected1

# Test case 2: Array with positive integers
arr2 = [1, 2, 3, 4, 5]
expected2 = 15
assert sum_arr(arr2) == expected2

# Test case 3: Array with negative integers
arr3 = [-1, -2, -3, -4, -5]
expected3 = -15
assert sum_arr(arr3) == expected3

# Test case 4: Array with both positive and negative integers
arr4 = [1, -2, 3, -4, 5]
expected4 = 3
assert sum_arr(arr4) == expected4

# Test case 5: Array with only one element
arr5 = [10]
expected5 = 10
assert sum_arr(arr5) == expected5

print("All test cases for summation passed!")


# Test case 1: Input file with numbers separated by letters
input_file_1 = io.StringIO('''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen''')

expected_output_1 = [12, 38, 15, 77, 29, 83, 13, 24, 42, 14, 76]
assert extract_num_input(input_file_1) == expected_output_1

# Test case 2: Input file with no numbers
input_file_2 = io.StringIO('''abcdefgh
ijklmnopq
rstuvwxyz''')

expected_output_2 = []
assert extract_num_input(input_file_2) == expected_output_2

# Test case 3: Input file with only one number per line
input_file_3 = io.StringIO('''1
2
3
4
5''')

expected_output_3 = [11, 22, 33, 44, 55]
assert extract_num_input(input_file_3) == expected_output_3

# Test case 4: Input file with numbers and non-alphanumeric characters
input_file_4 = io.StringIO('''1abc2!
pqr3stu8vwx@
a1b2c3d4e5f#
treb7uchet$
two1nine%
eightwothree^
abcone2threexyz&
xtwone3four*
4nineeightseven2(
zoneight234)
7pqrstsixteen_''')

expected_output_4 = [12, 38, 15, 77, 29, 83, 13, 24, 42, 14, 76]
assert extract_num_input(input_file_4) == expected_output_4

# Test case 5: Input file with overlapping regex matches.
input_file_5 = io.StringIO('''five6pvdsfiveone2threeddglqxqzqdxrnjkneightwox''')

expected_output_5 = [52]
assert extract_num_input(input_file_5) == expected_output_5

print("All test cases for part 2 of extraction passed!")

print("All test cases passed!")
