import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.Blind75.BitManipulation.SumOfTwoIntegers import SumOfTwoIntegers

def test_counting_bits():
    soti_instance = SumOfTwoIntegers()

    # Test case 1
    a = 1
    b = 2
    expected = 3
    assert soti_instance.getSum(a, b) == expected

    # Test case 2
    a = 2
    b = 3
    expected = 5
    assert soti_instance.getSum(a, b) == expected
