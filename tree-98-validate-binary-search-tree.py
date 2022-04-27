# @Time: 2022/4/26 16:54
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-98-validate-binary-search-tree.py
'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #method1, flatten this tree, check bad node
        #method
        self.found = False
        def isvalid(root, l, r):
            if root and not self.found:
                if root.val <= l  or root.val >= r:
                    self.found = True
                    return
                else:
                    isvalid(root.left, l, root.val)
                    isvalid(root.right, root.val, r)
        isvalid(root, -float("inf"), float("inf"))
        return not self.found