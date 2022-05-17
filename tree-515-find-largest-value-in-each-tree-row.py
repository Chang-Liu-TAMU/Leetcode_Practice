# @Time: 2022/5/12 18:22
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-515-find-largest-value-in-each-tree-row.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        ans = []
        while q:
            tem = []
            m = -float("inf")
            for i in q:
                if i.left:
                    tem.append(i.left)
                if i.right:
                    tem.append(i.right)
                if i.val > m:
                    m = i.val
            q = tem
            ans.append(m)
        return ans