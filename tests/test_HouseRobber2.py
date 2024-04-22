import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.HouseRobber2.HouseRobber2 import HouseRobber2

def test_house_robber():
    house_robber_instance = HouseRobber2()

    # Test case 1
    nums = [2,3,2]
    expected = 3
    assert house_robber_instance.rob(nums) == expected

    # Test case 2
    nums = [1,2,3,1]
    expected = 4
    assert house_robber_instance.rob(nums) == expected

    # Test case 3
    nums = [1,2,3]
    expected = 3
    assert house_robber_instance.rob(nums) == expected
