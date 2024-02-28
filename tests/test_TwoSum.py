import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.TwoSum.TwoSum import TwoSum

def test_two_sum():
    twoSum_instance = TwoSum()

    # Test case 1
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    assert twoSum_instance.twoSum(nums, target) == expected

    # Test case 2
    nums = [3, 2, 4]
    target = 6
    expected = [1, 2]
    assert twoSum_instance.twoSum(nums, target) == expected

    # Test case 3
    nums = [3, 3]
    target = 6
    expected = [0, 1]
    assert twoSum_instance.twoSum(nums, target) == expected