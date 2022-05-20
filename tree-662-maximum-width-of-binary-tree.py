# @Time: 2022/5/19 11:11
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-662-maximum-width-of-binary-tree.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [(root, 1)]
        ans = 1
        while q:
            tem = []
            for i, j in q:
                if i.left:
                    tem.append((i.left, j*2+1))
                if i.right:
                    tem.append((i.right, j*2+2))
            if tem:
                res = tem[-1][1] - tem[0][1] + 1
                ans = max(res, ans)
            q = tem
        return ans