# @Time: 2022/5/27 10:10
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:dp-62-latest-unique-paths.py


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0] * (n+1) for _ in range(m+1)]
        matrix[m-1][n-1] = 1
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r != m-1 or c != n-1:
                    matrix[r][c] = matrix[r+1][c] + matrix[r][c+1]
        return matrix[0][0]