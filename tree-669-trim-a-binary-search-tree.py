# @Time: 2022/5/19 11:33
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-669-trim-a-binary-search-tree.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root or low > high:
            return None
        if low <= root.val <= high:
            l = self.trimBST(root.left, low, root.val - 1)
            r = self.trimBST(root.right, root.val + 1, high)
            root.left = l
            root.right = r
            return root
        elif root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
