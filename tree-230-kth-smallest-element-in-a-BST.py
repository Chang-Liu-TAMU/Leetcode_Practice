# @Time: 2022/5/4 10:54
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-230-kth-smallest-element-in-a-BST.py


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            k -= 1
            root = stack.pop()
            if not k:
                return root.val
            root = root.right
