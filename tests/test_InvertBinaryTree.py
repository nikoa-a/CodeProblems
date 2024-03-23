import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.InvertBinaryTree.InvertBinaryTree import TreeNode, InvertBinaryTtree

def test_invert_binary_tree():
    invert_binary_tree_instance = InvertBinaryTtree()

    # Test case 1
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    expected = TreeNode(2)
    expected.left = TreeNode(3)
    expected.right = TreeNode(1)
    assert invert_binary_tree_instance.invertTree(root) == expected
