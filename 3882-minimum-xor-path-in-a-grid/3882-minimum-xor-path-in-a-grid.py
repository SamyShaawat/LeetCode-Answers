class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        F = (1 << 1024) - 1
        sh = []
        for b in range(10):
            w = 1 << b
            sh.append((w, ((1 << w) - 1) * (F // ((1 << (2 * w)) - 1))))
        n = len(grid[0])
        cur = [0] * n
        for i, r in enumerate(grid):
            for j, g in enumerate(r):
                if i == 0 and j == 0:
                    cur[0] = 1 << g
                    continue
                if i == 0:
                    s = cur[j - 1]
                elif j == 0:
                    s = cur[0]
                else:
                    s = cur[j] | cur[j - 1]
                for w, M in sh:
                    if g & w:
                        s = ((s & M) << w) | ((s >> w) & M)
                cur[j] = s
        s = cur[-1]
        return (s & -s).bit_length() - 1
