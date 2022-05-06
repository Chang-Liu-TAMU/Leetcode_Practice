# @Time: 2022/5/5 13:30
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-235-lowest-common-ancestor-of-a-binary-search-tree.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ptr = root
        x, y = (p.val, q.val) if p.val < q.val else (q.val, p.val)
        while ptr:
            if x <= ptr.val <= y:
                return ptr
            elif y < ptr.val:
                ptr = ptr.left
            else:
                ptr = ptr.right