class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SubtreeOfAnotherTree (object):

    def isSubtree(self, root, subroot):

        # Base case: if the subtree is None, it is a subtree of any tree
        if not subroot:
            return True
        
        # Base case: if the tree is None, it cannot contain a subtree
        if not root:
            return False
        
        # Check if the current tree is the same as the subtree
        if self.isSameTree(root, subroot):
            return True
        
        # Recursively check the left and right subtrees
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)
    
    # Helper function to check if two trees are the same
    def isSameTree(self, s, t):

        # Base case: if both trees are None, they are the same
        if not s and not t:
            return True
        
        # If one is None and the other is not, they are not the same
        if not s or not t:
            return False
        
        # If the values are different, they are not the same
        if s.val != t.val:
            return False
        
        # Recursively check the left and right subtrees
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
