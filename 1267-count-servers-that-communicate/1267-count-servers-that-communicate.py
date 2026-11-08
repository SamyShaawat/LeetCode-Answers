class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = [sum(r) for r in grid]
        cols = [sum(c) for c in zip(*grid)]
        ans = 0
        for i, r in enumerate(grid):
            if rows[i] > 1:
                ans += rows[i]
            else:
                for j, v in enumerate(r):
                    if v and cols[j] > 1:
                        ans += 1
                        break
        return ans
