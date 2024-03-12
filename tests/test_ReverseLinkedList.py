import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.ReverseLinkedList.ReverseLinkedList import ListNode, ReverseLinkedList

def test_reverse_linked_list():
    # Instantiate the ReverseLinkedList class
    rll_instance = ReverseLinkedList()

    # Test case 1
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Expected reversed linked list: 5 -> 4 -> 3 -> 2 -> 1
    expected_head = ListNode(5)
    expected_head.next = ListNode(4)
    expected_head.next.next = ListNode(3)
    expected_head.next.next.next = ListNode(2)
    expected_head.next.next.next.next = ListNode(1)

    # Check if the reversed linked list matches the expected result
    assert rll_instance.reverseLinkedList(head) == expected_head

    # Test case 2
    # Create a linked list: 1 -> 2
    head = ListNode(1)
    head.next = ListNode(2)

    # Expected reversed linked list: 2 -> 1
    expected_head = ListNode(2)
    expected_head.next = ListNode(1)

    # Check if the reversed linked list matches the expected result
    assert rll_instance.reverseLinkedList(head) == expected_head

    # Test case 3
    # Create an empty linked list
    head = None

    # Expected reversed linked list: None
    expected_head = None

    # Check if the reversed linked list matches the expected result
    assert rll_instance.reverseLinkedList(head) == expected_head
    