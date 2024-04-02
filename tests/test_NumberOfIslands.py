import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.NumberOfIslands.NumberOfIslands import NumberOfIslands

def test_number_of_islands():
    number_of_islands_instance = NumberOfIslands()

    # Test case 1
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    expected = 1
    assert number_of_islands_instance.numIslands(grid) == expected

    # Test case 2
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    expected = 3
    assert number_of_islands_instance.numIslands(grid) == expected
