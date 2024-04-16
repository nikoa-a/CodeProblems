import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.LongestSubstringWORepeatingChar.LongestSubstringWORepeatingChar import LongestSubstringWORepeatingChar

def test_longest_common_prefix():
    lswrc_instance = LongestSubstringWORepeatingChar()

    # Test case 1
    s = "abcabcbb"
    expected = 3
    assert lswrc_instance.lengthOfLongestSubstring(s) == expected

    # Test case 2
    s = "bbbbb"
    expected = 1
    assert lswrc_instance.lengthOfLongestSubstring(s) == expected

    # Test case 3
    s = "pwwkew"
    expected = 3
    assert lswrc_instance.lengthOfLongestSubstring(s) == expected
