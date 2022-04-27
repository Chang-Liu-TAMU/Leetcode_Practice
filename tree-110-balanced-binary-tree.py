# @Time: 2022/4/27 8:50
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-110-balanced-binary-tree.py

'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def help(root):
            if not root:
                return 0
            else:
                l = help(root.left)
                if l is None:
                    return
                r = help(root.right)
                if r is None:
                    return
                if abs(l - r) > 1:
                    return
                return 1 + max(l, r)
        return help(root) is not None