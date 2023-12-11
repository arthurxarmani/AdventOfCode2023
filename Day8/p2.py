import sys
import math
from functools import reduce


file = open(sys.argv[1], "r")
lines = file.readlines()

instructions = lines[0].strip()
lines.pop(0)
lines.pop(0)

maps = {}
for i in range(len(lines)):
    # A line looks like this:
    # AAA = (BBB, CCC)
    lines[i] = lines[i].strip()
    source = lines[i].split()[0]
    left = lines[i].split("(")[1].split(",")[0]
    right = lines[i].split(", ")[1].split(")")[0]
    maps[source] = {'L': left, 'R': right}


starting_locations = [key for key in maps.keys() if key.endswith("A")]

def apply_transformation(starting_location: str, starting_instruction_index: int, steps: int) -> (str, int):
    """
    Returns a new location with the transformation applied.
    Steps indicates how many instructions to follow.
    """
    current_index = starting_instruction_index
    current_location = starting_location
    current_step = 0
    while current_step < steps:
        if current_index >= len(instructions):
            current_index = 0
        
        current_location = maps[current_location][instructions[current_index]]
        current_index += 1
        current_step += 1
    
    return current_location, current_index

def apply_tranformation_until_z(starting_location: str, starting_instruction_index: int) -> (str, int, int):
    """
    Returns a new location with the transformation applied.
    Steps indicates how many instructions to follow.
    """
    # print("Starting instruction index: " + str(starting_instruction_index))
    current_index = starting_instruction_index
    current_location = starting_location
    transformations = 0
    while current_location[2] != "Z" or transformations == 0:
        if current_index >= len(instructions):
            current_index = 0
        current_location, current_index = apply_transformation(current_location, current_index, 1)
        transformations +=1
    if current_index >= len(instructions):
        current_index = 0
    return current_location, transformations

locs = starting_locations
transformations = []
indices = []
start_idx = 0
steps = 0

def lcm(x, y):
    """
    Calculate the least common multiple of two integers.
    """
    return x * y // math.gcd(x, y)

print("locs are" + str(locs))
for loc in locs:
    new_location, transformations_needed = apply_tranformation_until_z(loc, start_idx)   
    print("Entering main logic for " + loc)
    transformations.append(transformations_needed)
    print("Transformations: " + str(transformations))

# After all starting locations have been processed
# calculate least common multiple of transformations

print(reduce(lcm, transformations))