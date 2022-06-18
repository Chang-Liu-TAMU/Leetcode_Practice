# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.l = []
        self.d = 0
        def dfs(root, path, depth):
            path.append(root)
            if not root.left and not root.right:
                if depth == self.d:
                    self.l.append(list(path))
                elif depth > self.d:
                    self.d = depth
                    self.l = [list(path)]
            else:
                if root.left:
                    dfs(root.left, path, depth+1)
                if root.right:
                    dfs(root.right, path, depth+1)
            path.pop()
        dfs(root, [], 0)
        if len(self.l) == 1:
            return self.l[0][-1]
        for i in self.l:
            i.reverse()
        for nodes in zip(*self.l):
            s = set(nodes)
            if len(s) == 1:
                return s.pop()