# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(root, load):
            if not root:
                return 0
            r = dfs(root.right, load)
            v = root.val
            root.val += r + load
            l = dfs(root.left, root.val)
            return r + l + v
        dfs(root, 0)
        return root