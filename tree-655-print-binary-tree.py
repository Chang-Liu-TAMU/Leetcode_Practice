# @Time: 2022/5/17 14:02
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-655-print-binary-tree.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def println(self, root, r, c, ans):
        ans[r][c] = str(root.val)
        if root.left:
            self.println(root.left, r + 1, c - 2 ** (self.h - 2 - r), ans)
        if root.right:
            self.println(root.right, r + 1, c + 2 ** (self.h - 2 - r), ans)

    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        self.h = self.height(root)
        m = self.h
        n = 2 ** self.h - 1
        ans = [[""] * n for _ in range(m)]
        self.println(root, 0, (n - 1) // 2, ans)
        return ans