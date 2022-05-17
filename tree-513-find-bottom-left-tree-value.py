# @Time: 2022/5/11 15:26
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-513-find-bottom-left-tree-value.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = None
        q = [root]
        while q:
            ans = q[0].val
            tem = []
            for i in q:
                if i.left:
                    tem.append(i.left)
                if i.right:
                    tem.append(i.right)
            q = tem
        return ans