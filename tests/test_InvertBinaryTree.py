import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.InvertBinaryTree.InvertBinaryTree import TreeNode, InvertBinaryTtree

def test_invert_binary_tree():
    invert_binary_tree_instance = InvertBinaryTtree()

    # Test case 1
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    inverted_root1 = invert_binary_tree_instance.invertTree(root1)
    assert are_trees_equal(inverted_root1, TreeNode(2, TreeNode(3), TreeNode(1)))

    # Test case 2
    root2 = None
    inverted_root2 = invert_binary_tree_instance.invertTree(root2)
    assert are_trees_equal(inverted_root2, None)

    # Test case 3
    root3 = TreeNode(1)
    inverted_root3 = invert_binary_tree_instance.invertTree(root3)
    assert are_trees_equal(inverted_root3, TreeNode(1))


def are_trees_equal(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    return (tree1.val == tree2.val and
            are_trees_equal(tree1.left, tree2.left) and
            are_trees_equal(tree1.right, tree2.right))
