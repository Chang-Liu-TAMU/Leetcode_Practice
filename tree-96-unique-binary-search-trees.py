# @Time: 2022/4/26 16:47
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-96-unique-binary-search-trees.py
'''
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of
unique values from 1 to n.
'''

class Solution:
    def numTrees(self, n: int) -> int:
        def dp(m, memo):
            if m in [0, 1]:
                return 1
            if m in memo:
                return memo[m]
            ans = 0
            for i in range(m):
                l = dp(i, memo)
                r = dp(m-i-1, memo)
                ans += l * r
            memo[m] = ans
            return ans
        return dp(n, {})