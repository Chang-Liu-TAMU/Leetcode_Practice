# @Time: 2022/5/14 9:05
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-563-binary-tree-tilt.py


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.ans += abs(l - r)
            return l + r + root.val
        dfs(root)
        return self.ans