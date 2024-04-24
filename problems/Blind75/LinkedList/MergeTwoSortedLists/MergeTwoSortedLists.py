class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeTwoSortedLists (object):

    def mergeTwoLists(self, list1, list2):

        # Initialize a dummy node as the head of the merged list
        dummy = ListNode(-1)
        mergedCurrent = dummy

        # While both lists have nodes, compare the values of the nodes
        while list1 and list2:
            # Check which node has the smaller value
            if list1.val < list2.val:
                # Append the smaller node to the merged list
                mergedCurrent.next = list1
                # Move to the next node in list1
                list1 = list1.next
            else:
                # Append the smaller node to the merged list
                mergedCurrent.next = list2
                # Move to the next node in list2
                list2 = list2.next

            # Move to the next node in the merged list
            mergedCurrent = mergedCurrent.next

        # If either list1 or list2 still have nodes, append the remaining nodes to the merged list
        if list1:
            mergedCurrent.next = list1
        else:
            mergedCurrent.next = list2

        # Return the merged list excluding the dummy node
        return dummy.next
