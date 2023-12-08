import sys
import func


# Open the desired file from commandline input and extract necessary info.
input_file = open(sys.argv[1], 'r')
lines = input_file.readlines()
seeds, maps = func.extract_file_data(lines)

mapObjects = []

location_numbers = []

for map in maps:
    mapObjects.append(func.convert_to_map(map))


for seed in seeds:
    print("Processing seed: " + seed)
    for map in mapObjects:
        seed = func.convert_source_number(int(seed), map.ranges[0], map.ranges[1])
    location_numbers.append(seed)

location_numbers.sort()
print("The lowest location number was: " + str(location_numbers[0]))
