import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.ValidAnagram.ValidAnagram import ValidAnagram

def test_valid_anagram():
    valid_anagram_instance = ValidAnagram()

    # Test case 1
    s = "anagram"
    t = "nagaram"
    expected = True
    assert valid_anagram_instance.isAnagram(s, t) == expected

    # Test case 2
    s = "rat"
    t = "car"
    expected = False
    assert valid_anagram_instance.isAnagram(s, t) == expected
