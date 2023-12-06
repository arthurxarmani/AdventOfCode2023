from func import check_neighbors

def test_check_neighbors():
    # Test case 1: No symbols in neighbors
    neighbors = [['.', '.', '.'],
                 ['.', '.', '.'],
                 ['.', '.', '.']]
    assert check_neighbors(neighbors) == False

    # Test case 2: Symbol in the middle
    neighbors = [['.', '.', '.'],
                 ['.', '#', '.'],
                 ['.', '.', '.']]
    assert check_neighbors(neighbors) == True

    # Test case 3: Symbol at the top left corner
    neighbors = [['#', '.', '.'],
                 ['.', '.', '.'],
                 ['.', '.', '.']]
    assert check_neighbors(neighbors) == True

    # Test case 4: Symbol at the bottom right corner
    neighbors = [['.', '.', '.'],
                 ['.', '.', '.'],
                 ['.', '.', '#']]
    assert check_neighbors(neighbors) == True

    # Test case 5: Multiple symbols in different positions
    neighbors = [['#', '.', '#'],
                 ['.', '#', '.'],
                 ['#', '.', '#']]
    assert check_neighbors(neighbors) == True

    print("All test cases for check_neighbors passed!")    


def run_tests():
    test_check_neighbors()
    print("All tests passed!")


run_tests()

