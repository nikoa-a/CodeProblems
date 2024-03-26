import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.MergeTwoSortedLists.MergeTwoSortedLists import ListNode, MergeTwoSortedLists

def test_merge_two_sorted_lists():
    mtsl_instance = MergeTwoSortedLists()

    # Test case
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(4)
    head1 = ListNode(1)
    head1.next = ListNode(3)
    head1.next.next = ListNode(4)
    expected = ListNode(1)
    expected.next = ListNode(1)
    expected.next.next = ListNode(2)
    expected.next.next.next = ListNode(3)
    expected.next.next.next.next = ListNode(4)
    expected.next.next.next.next.next = ListNode(4)

    assert mtsl_instance.mergeTwoLists(head, head1) == expected
