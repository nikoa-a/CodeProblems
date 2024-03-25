class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InvertBinaryTtree(object):

    def invertTree(self, root):

        # Base case, if root is None, return None
        if not root:
            return None

        # Swap left and right children
        tempLeft = root.left
        root.left = root.right
        root.right = tempLeft

        # Recursively invert left and right children
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the root
        return root
