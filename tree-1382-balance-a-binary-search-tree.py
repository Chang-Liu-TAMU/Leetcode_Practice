# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(root, l):
            if root:
                dfs(root.left, l)
                l.append(root.val)
                dfs(root.right, l)
        l = []
        dfs(root, l)
        def construct(l, i, j):
            if i > j:
                return None
            if i == j:
                return TreeNode(l[i])
            m = (i + j) // 2
            root = TreeNode(l[m])
            root.left = construct(l, i, m-1)
            root.right = construct(l, m+1, j)
            return root
        return construct(l, 0, len(l)-1)