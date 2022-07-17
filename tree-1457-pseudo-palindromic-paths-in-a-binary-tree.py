# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(root, state):
            if root:
                v = root.val
                if state[v] == 0:
                    self.odd += 1
                    flag = 1
                elif state[v] % 2 == 0:
                    self.even -= 1
                    self.odd += 1
                    flag = 2
                else:
                    self.odd -= 1
                    self.even += 1
                    flag = 3
                state[v] += 1
                if not root.left and not root.right:
                    if self.odd <= 1:
                        self.ans += 1
                dfs(root.left, state)
                dfs(root.right, state)
                if flag == 1:
                    self.odd -= 1
                elif flag == 2:
                    self.odd -=1
                    self.even += 1
                else:
                    self.odd += 1
                    self.even -= 1
                state[v] -= 1
        self.odd = 0
        self.even = 0
        self.ans = 0
        dfs(root, defaultdict(int))
        return self.ans