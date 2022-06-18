# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.s = set(to_delete)
        self.ans = []

        def dfs(root, prev_del):
            if root:
                if root.val in to_delete:
                    dfs(root.left, True)
                    dfs(root.right, True)
                else:
                    if prev_del: self.ans.append(root)
                    dfs(root.left, False)
                    dfs(root.right, False)
                    if root.left and root.left.val in self.s:
                        root.left = None
                    if root.right and root.right.val in self.s:
                        root.right = None

        dfs(root, True)
        return self.ans

#         self.nodes = []
#         def dfs(root, prev):
#             if root:
#                 self.nodes.append(root)
#                 if root.val in to_delete:
#                     root.d = True
#                 else:
#                     root.d = False
#                 root.prev = prev
#                 dfs(root.left, root)
#                 dfs(root.right, root)

#         dfs(root, None)

#         def dfs_delete(root, lr):
#             if root:
#                 l, r = root.left, root.right
#                 if root.d:
#                     if root.prev:
#                         root.prev.__dict__[lr] = None
#                     if l:
#                         l.prev = None
#                     if r:
#                         r.prev = None
#                 dfs_delete(l, "left")
#                 dfs_delete(r, "right")
#         dfs_delete(root, None)
#         return [x for x in self.nodes if not x.d and not x.prev]