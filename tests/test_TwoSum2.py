import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.TwoSum2.TwoSum2 import TwoSum2

def test_two_sum():
    twoSum_instance = TwoSum2()

    # Test case 1
    nums = [2,7,11,15]
    target = 9
    expected = [1, 2]
    assert twoSum_instance.twoSum(nums, target) == expected

    # Test case 2
    nums = [2,3,4]
    target = 6
    expected = [1,3]
    assert twoSum_instance.twoSum(nums, target) == expected

    # Test case 3
    nums = [-1,0]
    target = -1
    expected = [1,2]
    assert twoSum_instance.twoSum(nums, target) == expected
