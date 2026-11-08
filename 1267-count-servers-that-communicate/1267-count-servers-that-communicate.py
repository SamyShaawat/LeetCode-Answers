class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        cols = list(map(sum, zip(*grid)))
        ans = 0
        for r in grid:
            s = sum(r)
            if s > 1:
                ans += s
            elif s and cols[r.index(1)] > 1:
                ans += 1
        return ans
