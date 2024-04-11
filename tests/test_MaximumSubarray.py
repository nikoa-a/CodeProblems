import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.MaximumSubarray.MaximumSubarray import MaximumSubarray

def test_maximum_subarray():
    maximum_subarray_instance = MaximumSubarray()

    # Test case 1
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    expected = 6
    assert maximum_subarray_instance.maxSubarray(nums) == expected

    # Test case 2
    nums = [1]
    expected = 1
    assert maximum_subarray_instance.maxSubarray(nums) == expected

    # Test case 3
    nums = [5,4,-1,7,8]
    expected = 23
    assert maximum_subarray_instance.maxSubarray(nums) == expected
