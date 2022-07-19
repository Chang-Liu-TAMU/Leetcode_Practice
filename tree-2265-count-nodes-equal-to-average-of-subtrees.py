# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0, 0
            lnum, lsum = dfs(root.left)
            rnum, rsum = dfs(root.right)
            allsum = lsum + rsum + root.val
            allnum = lnum + rnum + 1
            if root.val == floor(allsum / allnum):
                self.ans += 1
                # self.l.append(root.val)
            return allnum, allsum

        self.ans = 0
        # self.l = []
        dfs(root)
        # print(self.l)
        return self.ans