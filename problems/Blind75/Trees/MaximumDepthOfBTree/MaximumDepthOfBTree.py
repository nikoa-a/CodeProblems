class TreeNode:

    def __init__(self, val=0, left=None, right=None):    
        self.val = val
        self.left = left
        self.right = right


class MaximumDepthOfBTree (object):

    def maxDepth(self, root):

        # Base case: if the root is None, return 0 (depth of an empty subtree)
        if root is None:
            return 0

        # Recursive case: calculate the depth of the left subtree
        leftDepth = self.maxDepth(root.left)
        # Recursive case: calculate the depth of the right subtree
        rightDepth = self.maxDepth(root.right)
        # Return the maximum depth of either the left or right subtree, plus 1 for the current node
        return 1 + max(leftDepth, rightDepth)
    