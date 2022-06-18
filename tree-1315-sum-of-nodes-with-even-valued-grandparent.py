# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root, path):
            if root:
                path.append(root)
                if len(path) >= 3:
                    if path[-3].val % 2 == 0:
                        self.ans += root.val
                dfs(root.left, path)
                dfs(root.right, path)
                path.pop()
        dfs(root, [])
        return self.ans