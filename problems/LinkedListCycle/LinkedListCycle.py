class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedListCycle:

    def hasCycle(self, head):

        # Initialize slow and fast pointers. Slow pointer moves one step at a time while fast pointer moves two steps at a time.
        # 'fast' is fast pointer and 'head' is slow pointer.
        fast = head
        # Loop through the linked list until fast pointer reaches the end of the list.
        while fast and fast.next:
            # Move slow pointer one step at a time.
            head = head.next
            # Move fast pointer two steps at a time.
            fast = fast.next.next
            # If fast pointer meets slow pointer, a cycle is detected.
            if head is fast:
                return True

        # If fast pointer reaches the end of the list, then there is no cycle in the linked list.
        return False
