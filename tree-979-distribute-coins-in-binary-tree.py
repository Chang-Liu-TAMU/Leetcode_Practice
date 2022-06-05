# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(root, flag=False):
            if not root:
                return 0
            l = dfs(root.left, flag)
            r = dfs(root.right, flag)
            if not flag:
                root.ln = l
                root.rn = r
                return l + r + 1
            else:
                root.lc = l
                root.rc = r
                return l + r + root.val
        dfs(root)
        dfs(root, True)
        self.ans = 0
        def help(root, payload):
            if root:
                ln, rn, lc, rc = root.ln, root.rn, root.lc, root.rc
                diff = lc - ln
                mv = diff + root.val - 1 + payload
                self.ans += (abs(mv) + abs(diff))
                help(root.left, -diff)
                help(root.right, mv)
        help(root, 0)
        return self.ans