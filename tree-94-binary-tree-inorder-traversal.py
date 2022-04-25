# @Time: 2022/4/25 16:01
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-94-binary-tree-inorder-traversal.py
from typing import Optional, List
'''
Given the root of a binary tree,
return the inorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(root):
            if root:
                dfs(root.left)
                ans.append(root.val)
                dfs(root.right)
        dfs(root)
        return ans