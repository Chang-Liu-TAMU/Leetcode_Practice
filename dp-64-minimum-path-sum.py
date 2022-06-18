class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j, memo):
            t = (i, j)
            if i >= len(grid) or j >= len(grid[0]):
                return float("inf")
            if t in memo:
                return memo[t]
            if i == len(grid)-1 and j == len(grid[0])-1:
                return grid[-1][-1]
            ans = grid[i][j] + min(dfs(grid, i+1, j, memo), dfs(grid, i, j+1, memo))
            memo[t] = ans
            return ans
        return dfs(grid, 0, 0, {})