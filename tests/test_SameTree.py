import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.SameTree.SameTree import TreeNode, SameTree

def test_same_tree():
    same_tree_instance = SameTree()

    # Test case 1
    p = TreeNode(3)
    p.left = TreeNode(9)
    p.right = TreeNode(20)
    q = TreeNode(3)
    q.left = TreeNode(9)
    q.right = TreeNode(20)
    expected = True
    assert same_tree_instance.isSameTree(p, q) == expected

    # Test case 2
    p = TreeNode(5)
    p.left = TreeNode(8)
    p.left.right = TreeNode(15)
    q = TreeNode(5)
    q.left = TreeNode(9)
    expected = False
    assert same_tree_instance.isSameTree(p, q) == expected
