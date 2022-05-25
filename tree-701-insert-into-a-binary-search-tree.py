# @Time: 2022/5/24 9:48
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-701-insert-into-a-binary-search-tree.py


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new = TreeNode(val)
        if not root:
            return new
        ans = root
        while True:
            if root.val < val:
                if not root.right:
                    root.right = new
                    return ans
                else:
                    root = root.right
            else:
                if not root.left:
                    root.left = new
                    return ans
                else:
                    root = root.left