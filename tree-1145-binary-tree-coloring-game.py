# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        self.l = 0
        self.r = 0
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            res = l + r + 1
            if root.val == x:
                self.l = l
                self.r = r
            return res
        self.root = dfs(root)
        s = self.root - 1 - self.l - self.r
        b = [s-1, self.l - 1, self.r - 1]
        r = [self.l + self.r, self.r + s, self.l + s]
        return any(b > r for b, r in zip(b, r))