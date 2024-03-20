import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.ContainsDuplicate.ContainsDuplicate import ContainsDuplicate

def test_contains_duplicate():
    cd_instance = ContainsDuplicate()

    # Test case 1
    nums = [2,7,11,15]
    expected = False
    assert cd_instance.containsDuplicate(nums) == expected

    # Test case 2
    nums = [3,2,3,4]
    expected = True
    assert cd_instance.containsDuplicate(nums) == expected
    