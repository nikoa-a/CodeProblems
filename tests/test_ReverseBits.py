import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.ReverseBits.ReverseBits import ReverseBits

def test_reverse_bits():
    reverse_bits_instance = ReverseBits()

    # Test case 1
    n = int('00000010100101000001111010011100', 2)
    expected = 964176192
    assert reverse_bits_instance.reverseBits(n) == expected

    # Test case 2
    n = int('11111111111111111111111111111101', 2)
    expected = 3221225471
    assert reverse_bits_instance.reverseBits(n) == expected
