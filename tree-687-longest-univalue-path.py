# @Time: 2022/5/20 14:32
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-687-longest-univalue-path.py


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def help(root, target):
            if not root:
                return 0
            l = help(root.left, root.val)
            r = help(root.right, root.val)
            self.ans = max(self.ans, l + r)
            return 1 + max(l, r) if target == root.val else 0

        self.ans = 0
        help(root, root.val)
        return self.ans