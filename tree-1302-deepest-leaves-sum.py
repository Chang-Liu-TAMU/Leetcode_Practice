# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        self.ans = 0
        def dfs(root, d):
            if not root.left and not root.right:
                if d == self.d:
                    self.ans += root.val
                elif d > self.d:
                    self.d = d
                    self.ans = root.val
            else:
                if root.left:
                    dfs(root.left, d+1)
                if root.right:
                    dfs(root.right, d+1)
        dfs(root, 0)
        return self.ans