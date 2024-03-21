import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.LinkedListCycle.LinkedListCycle import ListNode, LinkedListCycle

def test_linked_list_cycle():

    llc_instance = LinkedListCycle()

    # Test case 1
    head = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    expected = True

    assert llc_instance.hasCycle(head) == expected

    # Test case 2
    head = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    head.next = node2
    node2.next = node3
    node3.next = node4

    expected = False

    assert llc_instance.hasCycle(head) == expected
