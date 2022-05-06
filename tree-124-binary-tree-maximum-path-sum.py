# @Time: 2022/4/28 20:24
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-124-binary-tree-maximum-path-sum.py
'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence
has an edge connecting them. A node can only appear in the sequence at most once. Note that the
path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
'''
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