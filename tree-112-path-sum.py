# @Time: 2022/4/27 9:11
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-112-path-sum.py

'''
Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path such that
adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.gotit = False

        def bt(root, path):
            if not self.gotit:
                path += root.val
                if not root.left and not root.right:
                    if path == targetSum:
                        self.gotit = True
                        return
                if root.left:
                    bt(root.left, path)
                if root.right:
                    bt(root.right, path)

        bt(root, 0)
        return self.gotit