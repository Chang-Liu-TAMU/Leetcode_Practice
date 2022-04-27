# @Time: 2022/4/26 17:24
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-100-same-tree.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif not q and not p:
            return True
        else:
            return False