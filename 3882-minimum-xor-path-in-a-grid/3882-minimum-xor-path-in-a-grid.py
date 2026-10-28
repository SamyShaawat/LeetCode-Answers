class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prev = None
        for i, r in enumerate(grid):
            cur = [None] * n
            for j, g in enumerate(r):
                if i == 0 and j == 0:
                    cur[0] = {g}
                    continue
                if i == 0:
                    s = cur[j - 1]
                elif j == 0:
                    s = prev[0]
                else:
                    s = prev[j] | cur[j - 1]
                cur[j] = {x ^ g for x in s}
            prev = cur
        return min(prev[-1])
