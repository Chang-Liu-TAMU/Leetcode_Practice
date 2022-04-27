# @Time: 2022/4/27 8:57
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-111-minimum-depth-of-binary-tree.py
'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def help(root):
            if not root.left and not root.right:
                return 1
            elif root.left and root.right:
                return 1 + min(help(root.left), help(root.right))
            elif root.left:
                return 1 + help(root.left)
            else:
                return 1 + help(root.right)
        if not root:
            return 0
        return help(root)