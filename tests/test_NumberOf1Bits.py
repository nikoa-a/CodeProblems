import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.NumberOf1Bits.NumberOf1Bits import NumberOf1Bits

def test_number_of_1_bits():
    no1b_instance = NumberOf1Bits()

    # Test case 1
    n = int('00000000000000000000000000001011', 2)
    expected = 3
    assert no1b_instance.hammingWeight(n) == expected

    # Test case 2
    n = int('00000000000000000000000010000000', 2)
    expected = 1
    assert no1b_instance.hammingWeight(n) == expected
    