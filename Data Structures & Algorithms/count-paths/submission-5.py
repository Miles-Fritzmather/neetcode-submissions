class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # grid = [[0 for i in range(0, n)] for j in range(0, m)]
        grid = [[0] * n] * m

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1: grid[i][j] = 1
                else:
                    below = grid[i][j + 1] if j < n - 1 else 0
                    right = grid[i + 1][j] if i < m - 1 else 0
                    grid[i][j] = below + right
        return grid[0][0]
