from collections import defaultdict

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        """
        suppose dp[i][j] yields the minimum cost to reach i, j
        then when k = 0, this is a dp problem where
        dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        """
        m, n = len(grid), len(grid[0])
        # construct the teleportation order
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[grid[i][j]].append((i, j))
        
        # construct costs for k = 0
        inf = float('inf')
        dp = [[inf] * n for _ in range(m)]
        dp[0][0] = 0
        def update():
            for i in range(m):
                for j in range(n):
                    temp = grid[i][j] + min(
                        dp[i-1][j] if i else inf, 
                        dp[i][j-1] if j else inf
                    )
                    if temp < dp[i][j]: dp[i][j] = temp
        update()

        # teleport k times
        keys = sorted(d, reverse=True)
        for _ in range(k):
            dist = inf
            for key in keys:
                for i, j in d[key]:
                    if dp[i][j] < dist: dist = dp[i][j]
                for i, j in d[key]:
                    dp[i][j] = dist
            update()
        return dp[-1][-1]