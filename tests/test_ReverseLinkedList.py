import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.ReverseLinkedList.ReverseLinkedList import ReverseLinkedList

def test_roman_to_integer():
    rll_instance = ReverseLinkedList()

    # Test case 1
    head = [1,2,3,4,5]
    expected = [5,4,3,2,1]
    assert rll_instance.reverseLinkedList(head) == expected

    # Test case 2
    head = [1,2]
    expected = [2,1]
    assert rll_instance.reverseLinkedList(head) == expected

    # Test case 3
    head = []
    expected = []
    assert rll_instance.reverseLinkedList(head) == expected
