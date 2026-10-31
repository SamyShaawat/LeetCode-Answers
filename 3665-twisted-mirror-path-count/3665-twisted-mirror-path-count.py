class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        M = 1000000007
        n = len(grid[0])
        b = [0] * n
        b[0] = 1
        t = 0
        for row in grid:
            nb = [0] * n
            a = 0
            for j in range(n):
                if row[j]:
                    nb[j] = a
                    a = b[j]
                else:
                    t = (a + b[j]) % M
                    a = nb[j] = t
            b = nb
        return t
