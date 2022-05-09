# @Time: 2022/5/8 11:22
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-404-sum-of-left-leaves.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def help(root, flag):
            if not root.left and not root.right and flag == "left":
                self.ans += root.val
                return
            if root.left:
                help(root.left, "left")
            if root.right:
                help(root.right, "right")
        help(root, None)
        return self.ans