import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.ValidPalindrome.ValidPalindrome import ValidPalindrome

def test_valid_palindrome():
    valid_palindrome_instance = ValidPalindrome()

    # Test case 1
    s = "A man, a plan, a canal: Panama"
    expected = True
    assert valid_palindrome_instance.isPalindrome(s) == expected

    # Test case 2
    s = "race a car"
    expected = False
    assert valid_palindrome_instance.isPalindrome(s) == expected
