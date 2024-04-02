import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.GroupAnagrams.GroupAnagrams import GroupAnagrams

def test_group_anagrams():
    group_anagrams_instance = GroupAnagrams()

    # Test case 1
    strs = ["eat","tea","tan","ate","nat","bat"]
    expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
    assert group_anagrams_instance.groupAnagrams(strs) == expected

    # Test case 2
    strs = [""]
    expected = [[""]]
    assert group_anagrams_instance.groupAnagrams(strs) == expected

    # Test case 3
    strs = ["a"]
    expected = [["a"]]
    assert group_anagrams_instance.groupAnagrams(strs) == expected
