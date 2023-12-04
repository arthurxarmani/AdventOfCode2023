from card import Card
from func import get_winning_numbers, is_equal_array, get_your_numbers

line_1 = "Card   1: 33 56 23 64 92 86 94  7 59 13 | 86 92 64 43 10 70 16 55 79 33 56  8  7 25 82 14 31 96 94 13 99 29 69 75 23"
expected_output_1 = [33, 56, 23, 64, 92, 86, 94, 7, 59, 13]

assert is_equal_array(get_winning_numbers(line_1), expected_output_1)

print("Test for get_winning_numbers passed!")


expected_output_2 = [86, 92, 64, 43, 10, 70, 16, 55, 79, 33, 56, 8, 7, 25, 82, 14, 31, 96, 94, 13, 99, 29, 69, 75, 23]
assert is_equal_array(get_your_numbers(line_1), expected_output_2)

print("Test for get_your_numbers passed!")

card = Card(get_winning_numbers(line_1), get_your_numbers(line_1))
expected_output_worth = 256
assert card.points_worth() == expected_output_worth

print("Test for points_worth passed!")