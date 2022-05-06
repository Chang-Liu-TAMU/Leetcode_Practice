# @Time: 2022/5/3 19:52
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-226-invert-binary-tree.py


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        tem = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tem)
        return root