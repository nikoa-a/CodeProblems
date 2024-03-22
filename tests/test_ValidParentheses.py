import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.ValidParentheses.ValidParentheses import ValidParentheses

def test_valid_parentheses():
    valid_parentheses_instance = ValidParentheses()

    # Test case 1
    s = "()"
    expected = True
    assert valid_parentheses_instance.isValid(s) == expected

    # Test case 2
    s = "()[]{}"
    expected = True
    assert valid_parentheses_instance.isValid(s) == expected

    # Test case 3
    s = "(]"
    expected = False
    assert valid_parentheses_instance.isValid(s) == expected
