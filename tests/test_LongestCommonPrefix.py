import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.LongestCommonPrefix.LongestCommonPrefix import LongestCommonPrefix

def test_roman_to_integer():
    lcp_instance = LongestCommonPrefix()

    # Test case 1
    strs = ["flower","flow","flight"]
    expected = "fl"
    assert lcp_instance.longestCommonPrefix(strs) == expected

    # Test case 2
    strs = ["dog","racecar","car"]
    expected = ""
    assert lcp_instance.longestCommonPrefix(strs) == expected
