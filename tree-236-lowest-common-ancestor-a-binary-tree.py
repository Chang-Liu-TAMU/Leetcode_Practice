# @Time: 2022/5/5 13:31
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-236-lowest-common-ancestor-a-binary-tree.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def help(root, path, t):
            if self.ans is None:
                path.append(root)
                if root.val == t.val:
                    self.ans = list(path)
                if root.left:
                    help(root.left, path, t)
                if root.right:
                    help(root.right, path, t)
                path.pop()
        self.ans = None
        help(root, [], p)
        a = self.ans
        self.ans = None
        help(root, [], q)
        b = set(self.ans)
        for i in range(-1, -len(a)-1, -1):
            x = a[i]
            if x in b:
                return x