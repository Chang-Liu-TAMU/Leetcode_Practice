# @Time: 2022/4/27 7:46
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-104-maximum-depth-of-binary-tree.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1