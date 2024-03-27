import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.SubtreeOfAnotherTree.SubtreeOfAnotherTree import TreeNode, SubtreeOfAnotherTree

def test_subtree_of_another_tree():
    soat_instance = SubtreeOfAnotherTree()

    # Test case
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    subroot = TreeNode(4)
    subroot.left = TreeNode(1)
    subroot.right = TreeNode(2)
    expected = True
    assert soat_instance.isSubtree(root, subroot) == expected
