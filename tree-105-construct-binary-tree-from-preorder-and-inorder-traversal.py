# @Time: 2022/4/27 7:51
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-105-construct-binary-tree-from-preorder-and-inorder-traversal.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        first = preorder[0]
        root = TreeNode(first)
        i = inorder.index(first)
        l = self.buildTree(preorder[1:1+i], inorder[:i])
        r = self.buildTree(preorder[1+i:], inorder[i+1:])
        root.left = l
        root.right = r
        return root