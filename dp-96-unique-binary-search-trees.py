class Solution:
    def numTrees(self, n: int) -> int:
        def dp(n, memo):
            if n == 0:
                return 1
            if n in memo:
                return memo[n]
            ans = 0
            for i in range(n):
                l = dp(i, memo)
                r = dp(n-i-1, memo)
                ans += l * r
            memo[n] = ans
            return ans
        return dp(n, {})