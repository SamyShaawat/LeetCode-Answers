class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)
        row_sum = 0
        for i in range(m - 1):
            row_sum += sum(grid[i])
            if row_sum * 2 == total_sum:
                return True
        col_sums = [0] * n
        for i in range(m):
            for j in range(n):
                col_sums[j] += grid[i][j]
        col_prefix = 0
        for j in range(n - 1):
            col_prefix += col_sums[j]
            if col_prefix * 2 == total_sum:
                return True
        return False