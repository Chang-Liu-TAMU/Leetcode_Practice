# @Time: 2022/4/27 10:54
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-114-flatten-binary-tree-to-linked-list.py



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def help(root):
            if not root:
                return (None, None)
            if not root.left and not root.right:
                return (root, root)
            lh, lt = help(root.left)
            rh, rt = help(root.right)
            root.left = None
            if not lh:
                root.right = rh
                return (root, rt)
            else:
                root.right = lh
                if not rh:
                    return (root, lt)
                else:
                    lt.right = rh
                    return (root, rt)
        help(root)