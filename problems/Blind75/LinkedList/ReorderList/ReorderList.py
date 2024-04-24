class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next


class ReorderList (object):

    def reorderList(self, head):
        
        # Initialize the slow and fast pointers
        slow = head
        fast = head.next 

        # Find the middle of the list. When fast reaches the end, slow will be at the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next     

        # Variables for reversing the second half of the list
        second = slow.next
        prev = None
        slow.next = None # Break the link to split the list into two halves

        # Reverse the second half of the list using the prev pointer and a temporary variable
        while second:
            # Store the next node in a temporary variable
            tmp = second.next
            # Set the next node to the previous node
            second.next = prev
            # Move the previous pointer to the current node
            prev = second
            # Move the current node to the next node
            second = tmp

        # Merge the first half and the reversed second half of the list
        # Initialize the first and second pointers 
        first = head
        second = prev
        # Iterate while the second pointer is not None
        while second:
            # Store the next nodes in temporary variables
            tmp1 = first.next
            tmp2 = second.next
            # Set the next node of the first pointer to the second pointer
            first.next = second
            # Set the next node of the second pointer to the next node of the first pointer
            second.next = tmp1
            # Move the first and second pointers to the next nodes
            first = tmp1
            second = tmp2
        
        return 
