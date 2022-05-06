# @Time: 2022/4/28 20:24
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:124-binary-tree-maximum-path-sum.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -float("inf")
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.ans = max(self.ans, l+root.val, r+root.val, root.val, root.val+l+r)
            return max(root.val, l+root.val, r+root.val)
        dfs(root)
        return self.ans