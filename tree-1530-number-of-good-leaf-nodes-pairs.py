# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
# method01
# Definition for a binary tree node.
# self.distance = distance
# self.ans = 0
# def help(root):
#     if not root.left and not root.right:
#         return [0]
#     elif root.left and root.right:
#         a, b = help(root.left), help(root.right)
#         for i in a:
#             for j in b:
#                 if i + j <= self.distance - 2:
#                     self.ans += 1
#         return [x+1 for x in a] + [x+1 for x in b]
#     else:
#         if root.left:
#             return [x+1 for x in help(root.left)]
#         else:
#             return [x+1 for x in help(root.right)]
# help(root)
# return self.ans
############################################################
# method02
        self.leaves = []
        def find_roots(root, parent):
            if root:
                find_roots(root.left, root)
                root.parent = parent
                if not root.left and not root.right:
                    self.leaves.append(root)
                find_roots(root.right, root)
        find_roots(root, None)

        self.pairs = 0

        def dfs(leave, level, seen):
            if leave not in seen:
                seen.add(leave)
            if not leave.left and not leave.right and level != 0:
                self.pairs += 1
            if level < distance:
                childs = [leave.parent, leave.left, leave.right]
                for i in childs:
                    if i and i not in seen:
                        dfs(i, level+1, seen)
        _ = [dfs(leave, 0, set()) for leave in self.leaves]
        return self.pairs // 2
