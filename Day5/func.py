from map import Map

def in_range(number, range_start, range_end):
    """
    Given a range, returns boolean if the number lies within the range, inclusive.
    """
    return number >= range_start and number <= range_end

def create_x_to_y_ranges(lines):
    """ 
    Given lines of a map, calculate the source and destination ranges.
    """
    source_ranges = []
    destination_ranges = []

    for line in lines:
        line = line.split()
        destination_range_start = int(line[0])
        source_range_start = int(line[1])
        range_length = int(line[2])

        destination_range_lower = destination_range_start
        destination_range_upper = destination_range_start + range_length - 1

        source_range_lower = source_range_start
        source_range_upper = source_range_start + range_length - 1

        destination_ranges.append([destination_range_lower, destination_range_upper])
        source_ranges.append([source_range_lower, source_range_upper])
    
    return source_ranges, destination_ranges

def convert_source_number(source_number: int, source_ranges, destination_ranges):
    """
    Given a source number, convert it to the destination number.
    """
    destination_value = None
    found_in_range = False
    for index in range(len(source_ranges)):
        if in_range(source_number, source_ranges[index][0], source_ranges[index][1]):
            found_in_range = True
            
            range_offset = destination_ranges[index][0] - source_ranges[index][0]
            destination_value = source_number + range_offset

    if not found_in_range: 
        return source_number
    return destination_value

def extract_file_data(lines):
    """
    Given a file, extract the seeds and the map.
    """
    seeds = []
    recording_map = False
    maps = []
    temp_map = []

    for line in lines:
        # Extract Seeds
        if line.startswith("seeds:"):
            seeds = (line.split(":")[1].split())
        
        # Extract Maps
        if line.endswith("map:\n"):
            recording_map = True
            continue

        if recording_map:
            if line == "\n":
                recording_map = False
                maps.append(temp_map)
                temp_map = []
                continue
            else:
                temp_map.append(line.strip())

    maps.append(temp_map)
    temp_map = []

    return seeds, maps

def extract_file_data_part_two(lines):
    """
    Given a file, extract the seeds and the map.
    Seeds are now in a range.
    First value is the starting number, the second is the range_length.
    """
    original_seeds = []
    recording_map = False
    maps = []
    temp_map = []
    new_seeds = []

    for line in lines:
        # Extract Seeds
        if line.startswith("seeds:"):
            original_seeds = (line.split(":")[1].split())
            for index in range(len(original_seeds)):
                if index % 2 == 0:
                    new_seeds.append([int(original_seeds[index]) , int(original_seeds[index]) + int(original_seeds[index + 1]) - 1])

        # Extract Maps
        if line.endswith("map:\n"):
            recording_map = True
            continue

        if recording_map:
            if line == "\n":
                recording_map = False
                maps.append(temp_map)
                temp_map = []
                continue
            else:
                temp_map.append(line.strip())

    maps.append(temp_map)
    temp_map = []
    return new_seeds, maps

def convert_to_map(text_map):
    return Map(create_x_to_y_ranges(text_map))

def revert_destination_number(destination_number: int, source_ranges, destination_ranges):
    """
    Given a destination number, revert it back to the source number.
    """
    source_value = None
    found_in_range = False
    for index in range(len(destination_ranges)):
        if in_range(destination_number, destination_ranges[index][0], destination_ranges[index][1]):
            found_in_range = True
            
            range_offset = destination_ranges[index][0] - source_ranges[index][0]
            source_value = destination_number - range_offset

    if not found_in_range: 
        return destination_number
    return source_value

def find_lowest_range(array):
    """
    Finds the lowest range in the 2D array, assuming range starts with lowest number.
    """
    lowest_number = None
    lowest_number_idx = None
    for index in range(len(array)):
        if lowest_number == None or array[index][0] < lowest_number:
            lowest_number = array[index][0]
            lowest_number_idx = index
    assert(lowest_number_idx != None)
    return array[lowest_number_idx]

def find_lowest_range_location_array(array):
    """
    Finds the lowest range in the 2D array, assuming range starts with lowest number.
    """
    lowest_number = None
    lowest_number_idx = None
    for index in range(len(array)):
        if lowest_number == None or array[index][1] < lowest_number or array[index][2] < lowest_number:
            lowest_number = min(array[index][1], array[index][2])
            lowest_number_idx = index
    assert(lowest_number_idx != None)
    return array[lowest_number_idx]