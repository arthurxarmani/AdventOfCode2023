import sys
import func

# Open the desired file from commandline input and extract necessary info.
input_file = open(sys.argv[1], 'r')
lines = input_file.readlines()
seeds, maps = func.extract_file_data_part_two(lines)

map_objects = []
for map in maps:
    map_objects.append(func.convert_to_map(map))


# We need to find the lowest seed number, so that we don't have to process all the seeds.
lowest_seed = func.find_lowest_range(seeds)[0]
print("Seed value must be greater or equal to " + str(lowest_seed))

for seed in seeds:
    print(seed)

found_match = False
lowest_location_number = 0 
while not found_match:
    print("Processing lowest location number: " + str(lowest_location_number))
    temp_location_number = lowest_location_number
    for map in reversed(map_objects):
        temp_location_number = func.revert_destination_number(temp_location_number, map.ranges[0], map.ranges[1])
    print ("reverted seed: " + str(temp_location_number))
    reverted_seed = temp_location_number
    if reverted_seed >= lowest_seed:
        for pair in seeds:
            print("checking if reverted seed " + str(reverted_seed) + " is in seeds: " + str(pair))
            
            if func.in_range(reverted_seed, pair[0], pair[1]):
                found_match = True
                print("Found something...")
                print("at " + str(lowest_location_number))
                break
    
    lowest_location_number += 1000

# process_lower_thousand
lowest_location_number -= 2000
found_match = False
while not found_match:
    print("Processing lowest location number: " + str(lowest_location_number))
    temp_location_number = lowest_location_number
    for map in reversed(map_objects):
        temp_location_number = func.revert_destination_number(temp_location_number, map.ranges[0], map.ranges[1])
    print ("reverted seed: " + str(temp_location_number))
    reverted_seed = temp_location_number
    if reverted_seed >= lowest_seed:
        for pair in seeds:
            print("checking if reverted seed " + str(reverted_seed) + " is in seeds: " + str(pair))
            
            if func.in_range(reverted_seed, pair[0], pair[1]):
                found_match = True
                print("++========reverted location number is greater than or equal to lowest seed!")
                print("The lowest location number was: " + str(lowest_location_number))
                break
    
    lowest_location_number += 1