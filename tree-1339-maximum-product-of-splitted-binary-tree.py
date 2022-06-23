# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            s = dfs(root.left) + dfs(root.right) + root.val
            root.s = s
            return s

        dfs(root)

        self.ans = 0
        s = root.s

        def help(root):
            if root.left:
                v = (s - root.left.s) * root.left.s
                self.ans = max(self.ans, v)
                help(root.left)
            if root.right:
                v = (s - root.right.s) * root.right.s
                self.ans = max(self.ans, v)
                help(root.right)

        help(root)
        return self.ans % (10 ** 9 + 7)
