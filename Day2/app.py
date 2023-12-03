import sys
import func


"""
Open the file specified by the first argument.
Extract game ids from the file which meet the criteria.
Sum the result.
"""
input_file = open(sys.argv[1], 'r')
game_ids = func.extract_valid_game_ids(input_file)
input_file.close()

print("sum: " + str(func.sum_arr(game_ids)))


"""
Open the file specified by the first argument.
Extract power from all games.
Sum the result.
"""
input_file = open(sys.argv[1], 'r')
powers = func.extract_powers(input_file)
input_file.close()

print("sum: " + str(func.sum_arr(powers)))
