class Solution:
    def numDecodings(self, s: str) -> int:
        def dp(s, memo, i):
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            if i == len(s)-1:
                return 1
            if i in memo:
                return memo[i]
            a = dp(s, memo, i+1)
            if i <= len(s)-2:
                if int(s[i:i+2]) <= 26:
                    a += dp(s, memo, i+2)
            memo[i] = a
            return a
        return dp(s, {}, 0)