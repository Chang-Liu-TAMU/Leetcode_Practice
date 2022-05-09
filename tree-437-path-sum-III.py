# @Time: 2022/5/8 11:45
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-437-path-sum-III.py


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import chain


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        self.t = targetSum

        def dfs(root):
            if not root: return []
            l = dfs(root.left)
            r = dfs(root.right)
            tem = []
            for i in chain(l, r, [0]):
                ans = i + root.val
                if ans == self.t:
                    self.ans += 1
                tem.append(ans)
            return tem

        dfs(root)
        return self.ans
