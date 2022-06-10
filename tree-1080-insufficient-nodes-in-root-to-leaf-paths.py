# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(root, path):
            path.append(root.val)
            if not root.left and not root.right:
                tem = [sum(path)]
                path.pop()
                return tem
            l, r = [], []
            if root.left:
                l = dfs(root.left, path)
            if root.right:
                r = dfs(root.right, path)
            if not any([x >= self.limit for x in l]):
                root.left = None
            if not any([x >= self.limit for x in r]):
                root.right = None
            merge = l + r
            path.pop()
            return merge

        self.limit = limit
        tem = dfs(root, [])
        if not any([x >= self.limit for x in tem]):
            return None
        return root
        # slow solution
#         def dfs(root, v):
#             if not root:
#                 return []

#             l = dfs(root.left, v+root.val)
#             r = dfs(root.right,  v+root.val)
#             if not l and not r:
#                 if v + root.val < limit:
#                     self.d.add(root)
#                 return [root.val]
#             else:
#                 l.extend(r)
#                 flag = True
#                 for i in range(len(l)):
#                     l[i] += root.val
#                     if l[i] + v >= limit:
#                         flag = False
#                 if flag:
#                     self.d.add(root)
#                 return l

#         self.d = set()
#         dfs(root, 0)
#         if root in self.d:
#             return None
#         q = [root]
#         while q:
#             tem = []
#             for i in q:
#                 if i.left:
#                     if i.left in self.d:
#                         i.left = None
#                     else:
#                         tem.append(i.left)
#                 if i.right:
#                     if i.right in self.d:
#                         i.right = None
#                     else:
#                         tem.append(i.right)
#             q = tem
#         return root