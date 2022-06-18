class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dfs(grid, i, j, memo):
            t = (i, j)
            if t in memo:
                return memo[t]

            if i >= len(grid) or j >= len(grid[0]):
                return 0
            if grid[i][j] == 1:
                return 0
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return 1
            ans = dfs(grid, i + 1, j, memo) + dfs(grid, i, j + 1, memo)
            memo[t] = ans
            return ans

        return dfs(obstacleGrid, 0, 0, {})