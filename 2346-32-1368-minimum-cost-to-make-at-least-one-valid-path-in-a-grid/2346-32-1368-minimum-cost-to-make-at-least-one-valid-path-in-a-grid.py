class Solution:
    def minCost(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        tch = [(0, 0)]
        dkr = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

        res = 0
        while True:
            ntch = []
            for i, j in tch:
                ni, nj = i, j
                while -1 < ni < m and -1 < nj < n and grid[ni][nj]:
                    if ni == m - 1 and nj == n - 1:
                        return res
                    if ni - 1 > -1:
                        ntch.append((ni - 1, nj))
                    if ni + 1 < m:
                        ntch.append((ni + 1, nj))
                    if nj - 1 > -1:
                        ntch.append((ni, nj - 1))
                    if nj + 1 < n:
                        ntch.append((ni, nj + 1))
                    xni,xnj = ni,nj
                    ni, nj = ni + dkr[grid[ni][nj]][0], nj + dkr[grid[ni][nj]][1]
                    grid[xni][xnj] = 0

            tch = []
            for i, j in ntch:
                if grid[i][j]:
                    tch.append((i, j))
            res += 1
        return res