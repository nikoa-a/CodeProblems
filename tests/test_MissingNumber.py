import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.MissingNumber.MissingNumber import MissingNumber

def test_meeting_rooms():
    missing_number_instance = MissingNumber()

    # Test case 1
    nums = [3,0,1]
    expected = 2
    assert missing_number_instance.missingNumber(nums) == expected

    # Test case 2
    nums = [0,1]
    expected = 2
    assert missing_number_instance.missingNumber(nums) == expected

    # Test case 3
    nums = [9,6,4,2,3,5,7,0,1]
    expected = 8
    assert missing_number_instance.missingNumber(nums) == expected
