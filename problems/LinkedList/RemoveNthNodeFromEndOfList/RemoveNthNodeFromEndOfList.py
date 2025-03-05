class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class RemoveNthNodeFromEndOfList (object):

    def removeNthFromEnd(self, head, n):

        # Initialize a dummy node as the head of the list
        dummy = ListNode(0, head)
        # Initialize left pointer to dummy node
        left = dummy

        # Initialize right pointer to head plus n nodes
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1

        # Move both pointers until right reaches the end of the list
        while right:
            left = left.next
            right = right.next

        # Remove the nth node from the end of the list by updating the next pointer of the left node
        left.next = left.next.next

        # Return the list excluding the dummy node which is the head of the list
        return dummy.next
