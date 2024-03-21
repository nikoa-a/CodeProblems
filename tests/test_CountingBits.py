import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.CountingBits.CountingBits import CountingBits

def test_counting_bits():
    counting_bits_instance = CountingBits()

    # Test case 1
    n = 2
    expected = [0,1,1]
    assert counting_bits_instance.countBits(n) == expected

    # Test case 2
    n = 5
    expected = [0,1,1,2,1,2]
    assert counting_bits_instance.countBits(n) == expected
