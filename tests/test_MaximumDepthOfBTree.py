import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.MaximumDepthOfBTree.MaximumDepthOfBTree import TreeNode, MaximumDepthOfBTree

def test_maximum_depth_of_binary_tree():
    mdobt_instance = MaximumDepthOfBTree()

    # Test case 1
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    expected = 3
    assert mdobt_instance.maxDepth(root) == expected

    # Test case 2
    root = TreeNode(1)
    root.right = TreeNode(2)
    expected = 2
    assert mdobt_instance.maxDepth(root) == expected
