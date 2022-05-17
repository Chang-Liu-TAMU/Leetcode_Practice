# @Time: 2022/5/12 20:38
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-538-convert-BST-to-Greater-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.val = 0
        def dfs(root):
            if not root:
                return 0
            r = dfs(root.right)
            tem = self.val
            self.val += root.val
            root.val += tem
            l = dfs(root.left)

        dfs(root)
        return root