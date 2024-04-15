import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.ContainerWithMostWater.ContainerWithMostWater import ContainerWithMostWater

def test_contains_duplicate():
    cwmw_instance = ContainerWithMostWater()

    # Test case 1
    height = [1,8,6,2,5,4,8,3,7]
    expected = 49
    assert cwmw_instance.maxArea(height) == expected

    # Test case 2
    height = [1,1]
    expected = 1
    assert cwmw_instance.maxArea(height) == expected
