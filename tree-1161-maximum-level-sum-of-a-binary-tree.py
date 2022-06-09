# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        m = 1
        ans = -float("inf")
        q = [root]
        level = 1
        while q:
            tem = []
            s = 0
            for i in q:
                if i.left:
                    tem.append(i.left)
                if i.right:
                    tem.append(i.right)
                s += i.val
            if s > ans:
                ans = s
                m = level
            level += 1
            q = tem
        return m
