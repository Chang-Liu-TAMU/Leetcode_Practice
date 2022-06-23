# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dp(i, j, memo):
            if i > j:
                return [None]
            if (i, j) in memo:
                return memo[(i, j)]
            if i == j:
                return [TreeNode(i)]
            res = []
            for k in range(i, j + 1):
                l = dp(i, k - 1, memo)
                r = dp(k + 1, j, memo)
                for x in l:
                    for y in r:
                        res.append(TreeNode(k, x, y))

            memo[i, j] = res
            return res

        return dp(1, n, {})