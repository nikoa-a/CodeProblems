import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.PalindromeNumber.PalindromeNumber import PalindromeNumber

def test_palindrome_number():
    palindromeNumber_instance = PalindromeNumber()

    # Test case 1
    x = 121
    expected = True
    assert palindromeNumber_instance.isPalindrome(x) == expected

    # Test case 2
    x = -121
    expected = False
    assert palindromeNumber_instance.isPalindrome(x) == expected

    # Test case 3
    x = 10
    expected = False
    assert palindromeNumber_instance.isPalindrome(x) == expected