import func
from game import Game 
import io


input_string_1 = "Game 1: 18 red, 8 green, 7 blue; 15 red, 4 blue, 1 green; 2 green, 17 red, 6 blue; 5 green, 1 blue, 11 red; 18 red, 1 green, 14 blue; 8 blue"
expected_output_1 = 1
assert func.extract_id(input_string_1) == expected_output_1

input_string_2 = "Game 15: 18 red, 8 green, 7 blue; 15 red, 4 blue, 1 green; 2 green, 17 red, 6 blue; 5 green, 1 blue, 11 red; 18 red, 1 green, 14 blue; 8 blue"
expected_output_2 = 15
assert func.extract_id(input_string_2) == expected_output_2

print("Tests for extract_id passed!")

"""
We can have up to 12 red cubes, 13 green cubes, and 14 blue cubes.
"""
game_1 = Game(18, 8, 7)
game_2 = Game(15, 4, 1)
game_3 = Game(2, 17, 6)
game_4 = Game(5, 1, 11)
game_5 = Game(1, 1, 15)
assert game_1.is_possible() == False
assert game_2.is_possible() == False
assert game_3.is_possible() == False
assert game_4.is_possible() == True
assert game_5.is_possible() == False

print("Tests for is_possible passed!")


input_string_1 = "Game 1: 18 red, 8 green, 7 blue; 15 red, 4 blue, 1 green; 2 green, 17 red, 6 blue; 5 green, 1 blue, 11 red; 18 red, 1 green, 14 blue; 8 blue"
input_string_2 = "Game 23: 6 green, 4 red, 3 blue; 1 blue, 2 red, 9 green; 5 green, 1 red, 3 blue; 5 blue, 4 red, 4 green"
input_string_3 = "Game 30: 11 blue, 17 green, 10 red; 9 blue, 12 green, 14 red; 16 green, 2 red, 8 blue; 18 green, 1 red, 1 blue; 5 blue, 7 red, 18 green; 9 green, 3 blue, 11 red"

expected_output_1 = [Game(18, 8, 7), Game(15, 1, 4), Game(17, 2, 6), Game(11, 5, 1), Game(18, 1, 14), Game(0, 0, 8)]
expected_output_2 = [Game(4, 6, 3), Game(2, 9, 1), Game(1, 5, 3), Game(4, 4, 5)]
expected_output_3 = [Game(10, 17, 11), Game(14, 12, 9), Game(2, 16, 8), Game(1, 18, 1), Game(7, 18, 5), Game(11, 9, 3)]

assert func.extract_cubes(input_string_1) == expected_output_1
assert func.extract_cubes(input_string_2) == expected_output_2
assert func.extract_cubes(input_string_3) == expected_output_3

print("Tests for extract_cubes passed!")

input_file_1 = io.StringIO(input_string_1+"\n"+input_string_2+"\n"+input_string_3)
expected_output_1 = [23]
assert func.is_equal_array(func.extract_valid_game_ids(input_file_1), expected_output_1)

print("Test for extract_valid_game_ids passed!")

power_input_1 = [Game(18, 8, 7), Game(15, 1, 4), Game(17, 2, 6), Game(11, 5, 1), Game(18, 1, 14), Game(0, 0, 8)]
expected_power_output_1 = 2016
assert func.extract_power(power_input_1) == expected_power_output_1
print("Test for extract_power passed!")

input_file_2 = io.StringIO("""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""")
expected_result_2 = [48, 12, 1560, 630, 36]
assert func.is_equal_array(func.extract_powers(input_file_2), expected_result_2)
print("Test for extract_powers passed!")

print("All tests passed!")