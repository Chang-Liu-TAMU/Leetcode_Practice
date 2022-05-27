# @Time: 2022/5/25 9:22
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-814-binary-tree-pruning.py


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        l = self.pruneTree(root.left)
        r = self.pruneTree(root.right)
        if l or r:
            root.left = l
            root.right = r
            return root
        else:
            if root.val != 1:
                return None
            else:
                root.left = None
                root.right = None
                return root
