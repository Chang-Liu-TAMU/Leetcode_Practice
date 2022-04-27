# @Time: 2022/4/26 17:17
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-99-recover-binary-search-tree.py
'''
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake.
Recover the tree without changing its structure.
'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        l = []

        def dfs(root):
            if root:
                dfs(root.left)
                l.append(root)
                dfs(root.right)

        dfs(root)
        a, b = None, None
        for i in range(len(l)):
            if l[i].val >= l[i + 1].val:
                a = i
                break
        for i in range(-1, -len(l), -1):
            if l[i].val <= l[i - 1].val:
                b = i
                break
        l[a].val, l[b].val = l[b].val, l[a].val
