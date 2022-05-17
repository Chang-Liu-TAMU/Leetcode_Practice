# @Time: 2022/5/11 15:23
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-508-most-frequent-subtree-sum.py


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if not root:
                return 0
            ans = root.val + dfs(root.left) + dfs(root.right)
            self.d[ans] += 1
            return ans
        self.d = defaultdict(int)
        dfs(root)
        t = max(self.d.values())
        return [key for key in self.d if self.d[key] == t]