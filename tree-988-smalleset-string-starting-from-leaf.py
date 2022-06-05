# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = "~"
        def dfs(root, l):
            if root:
                l.append(chr(root.val + ord("a")))
                if not root.left and not root.right:
                    self.ans = min(self.ans, "".join(reversed(l)))
                else:
                    dfs(root.left, l)
                    dfs(root.right, l)
                l.pop()
        dfs(root, [])
        return self.ans