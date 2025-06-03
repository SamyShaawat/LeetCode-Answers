class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if j < n - 1 and grid[i][j] == grid[i][j + 1]:
                    return False
                if i < m - 1 and grid[i][j] != grid[i + 1][j]:
                    return False
        return True