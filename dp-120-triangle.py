class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def dp(i, j, memo):
            if i == len(triangle) - 1:
                return triangle[i][j]
            if (i, j) in memo:
                return memo[(i, j)]
            ans = min(dp(i + 1, j, memo), dp(i + 1, j + 1, memo)) + triangle[i][j]
            memo[(i, j)] = ans
            return ans

        return dp(0, 0, {})