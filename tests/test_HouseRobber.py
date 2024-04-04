import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.HouseRobber.HouseRobber import HouseRobber

def test_house_robber():
    house_robber_instance = HouseRobber()

    # Test case 1
    nums = [1,2,3,1]
    expected = 4
    assert house_robber_instance.rob(nums) == expected

    # Test case 2
    nums = [2,7,9,3,1]
    expected = 12
    assert house_robber_instance.rob(nums) == expected
