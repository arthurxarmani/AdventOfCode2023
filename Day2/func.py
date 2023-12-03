import regex as re
from game import Game


def extract_id(line): 
    """ 
    Extracts the id from the input line by using regex.
    The input is expected to be in the form of Game <id>: ...
    """
    game_id = line.split(":")[0]
    game_id = re.findall(r'\d+', game_id)[0]

    return int(game_id)


def extract_cubes(line): 
    """ 
    Extracts the cubes from the input line by using regex.
    The input is expected to be in the form of Game <id>: <red> red, <green> green, <blue> blue; ...
    The cubes can appear in any order.
    """
    # First, we extract all the results from the input line.
    all_results = line.split(": ")[1]
    # Then, we split the results by the semicolon.
    all_results = all_results.split(";")
    games = []
    for result in all_results:
        red = re.findall(r'\d+ red', result)
        green = re.findall(r'\d+ green', result)
        blue = re.findall(r'\d+ blue', result)
        if red == []: 
            red = 0
        else:
            red = red[0].split()[0]
        if green == []:
            green = 0
        else:
            green = green[0].split()[0]
        if blue == []:
            blue = 0
        else: 
            blue = blue[0].split()[0]
        games.append(Game(red, green,blue))
    return games

def sum_arr(arr):
    """
    Sums the elements in an array
    """
    sum = 0

    for i in arr:
        sum += i

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

def extract_valid_game_ids(input_file):
    """
    Extracts the valid game ids from the input file.
    A game_id is added only if all individual cube draws are possible.
    """
    valid_game_ids = []
    lines = input_file.readlines()
    for line in lines: 
        game_id = extract_id(line)
        game_values = extract_cubes(line)
        game_possible = True
        for draw in game_values: 
            if not draw.is_possible():
                game_possible = False
                break 
        if game_possible:
            valid_game_ids.append(int(game_id))
    return valid_game_ids

def extract_power(games):
    """
    Extracts the power of a game.
    The power of a game is a multiple of the highest number of red, green and blue cubes.
    """
    power = 0
    highest_red = 0
    highest_blue = 0
    highest_green = 0
    for game in games:
        if game.red > highest_red:
            highest_red = game.red
        if game.blue > highest_blue:
            highest_blue = game.blue
        if game.green > highest_green:
            highest_green = game.green
    power = highest_red * highest_blue * highest_green
    return power

def extract_powers(input_file):
    """
    Extracts the powers of all games in the input file.
    """
    powers = []
    lines = input_file.readlines()
    for line in lines:
        game_values = extract_cubes(line)
        powers.append(extract_power(game_values))
    return powers
