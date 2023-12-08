import func

def test_in_range():
    range_1 = [1, 3]
    range_2 = [4, 6]
    range_3 = [100, 500]

    assert func.in_range(2, range_1[0], range_1[1]) == True
    assert func.in_range(4, range_1[0], range_1[1]) == False
    assert func.in_range(5, range_2[0], range_2[1]) == True
    assert func.in_range(99, range_3[0], range_3[1]) == False
    assert func.in_range(100, range_3[0], range_3[1]) == True
    assert func.in_range(500, range_3[0], range_3[1]) == True
    print("All test cases for in_range passed!")
test_in_range()


def test_map_range_extraction():
    input_file = open("testmap.txt", "r")
    lines = input_file.readlines()
    source_range_expected = [[98, 99], [50, 97]]
    destination_range_expected = [[50, 51], [52, 99]]
    source_range_actual, destination_range_actual = func.create_x_to_y_ranges(lines)

    assert func.create_x_to_y_ranges(lines) == (source_range_expected, destination_range_expected)
    print("Test for map range extraction passed!")
test_map_range_extraction()


def test_conversion():
    input_file = open("testmap.txt", "r")
    lines = input_file.readlines()
    seed = 79
    soil = 81
    seed_ranges, soil_ranges = func.create_x_to_y_ranges(lines)
    assert func.convert_source_number(seed, seed_ranges, soil_ranges) == soil
    print("Test for conversion passed!")
test_conversion()

def test_reversion():
    input_file = open("testmap.txt", "r")
    lines = input_file.readlines()
    seed = 79
    soil = 81
    seed_ranges, soil_ranges = func.create_x_to_y_ranges(lines)
    assert func.revert_destination_number(soil, seed_ranges, soil_ranges) == seed
    print("Test 1 for reversion passed!")


    input_file_2 = open("fertilizer-to-water-map.txt", "r")
    lines = input_file_2.readlines()
    fertilizer = 81
    water = 81
    water_ranges, fertilizer_ranges = func.create_x_to_y_ranges(lines)
    assert func.revert_destination_number(water, fertilizer_ranges, water_ranges) == fertilizer

    print("Tests for reversion passed!")
test_reversion()