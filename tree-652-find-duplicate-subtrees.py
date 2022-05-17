# @Time: 2022/5/16 11:59
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-652-find-duplicate-subtrees.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dups = set()
        d = {}

        def dfs(root):
            if not root:
                return "None"
            sig = str(root.val) + "l" + dfs(root.left) + "r" + dfs(root.right)
            if sig in d:
                dups.add(d[sig])
            else:
                d[sig] = root
            return sig

        dfs(root)
        return list(dups)
