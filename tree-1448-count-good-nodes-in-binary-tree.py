# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, p):
            if root:
                if not p:
                    p.append(root.val)
                else:
                    if root.val > p[-1]:
                        p.append(root.val)
                    else:
                        p.append(p[-1])
                if root.val >= p[-1]:
                    self.ans += 1
                dfs(root.left, p)
                dfs(root.right, p)
                p.pop()
        self.ans = 0
        dfs(root, [])
        return self.ans