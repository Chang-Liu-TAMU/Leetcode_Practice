# @Time: 2022/4/26 17:28
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-101-symmetric-tree.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(l, r):
            if not l and not r:
                return True
            elif l and r:
                if l.val != r.val:
                    return False
                else:
                    return mirror(l.left, r.right) and mirror(l.right, r.left)
            else:
                return False
        return mirror(root.left, root.right)