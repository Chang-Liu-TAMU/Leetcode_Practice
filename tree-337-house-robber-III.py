# @Time: 2022/5/6 18:41
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-337-house-robber-III.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def help(root, memo):
            if not root:
                return 0
            if root in memo:
                return memo[root]
            x = root.val
            if root.left:
                x += help(root.left.left, memo) + help(root.left.right, memo)
            if root.right:
                x += help(root.right.left, memo) + help(root.right.right, memo)

            y = help(root.left, memo) + help(root.right, memo)
            ans = max(x, y)
            memo[root] = ans
            return ans

        return help(root, {})