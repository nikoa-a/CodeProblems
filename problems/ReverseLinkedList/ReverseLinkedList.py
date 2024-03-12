class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    
    def __eq__(self, other):
        # Check if 'other' is an instance of ListNode
        if not isinstance(other, ListNode):
            return False
        # Check if the 'val' attributes of both nodes are equal
        # and if their 'next' attributes point to the same node or are both None
        return self.val == other.val and self.next == other.next


class ReverseLinkedList (object):

    def reverseLinkedList(self, head):

        # 'newHead' always points to the head of the reversed list
        newHead = None
        # 'current' is the pointer to create the reversed list, initially it points to the head of the original list
        current = head

        while current:
            # 'nextNode' is used to store the next node in the original list
            nextNode = current.next
            # current.next is now the head of the reversed list
            current.next = newHead
            # newHead becomes the current node in the original list
            newHead = current
            # Move to the next node in the original list
            current = nextNode

        # Return the head of the reversed list
        return newHead
