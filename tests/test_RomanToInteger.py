import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.RomanToInteger.RomanToInteger import RomanToInteger

def test_roman_to_integer():
    romanToInt_instance = RomanToInteger()

    # Test case 1
    string = "III"
    expected = 3
    assert romanToInt_instance.romanToInt(string) == expected

    # Test case 2
    string = "LVIII"
    expected = 58
    assert romanToInt_instance.romanToInt(string) == expected

    # Test case 3
    string = "MCMXCIV"
    expected = 1994
    assert romanToInt_instance.romanToInt(string) == expected