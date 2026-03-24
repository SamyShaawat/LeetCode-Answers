class Solution:
    def constructProductMatrix(self, grid):
        m, n = len(grid), len(grid[0])
        arr = [grid[i][j] for i in range(m) for j in range(n)]

        size = len(arr)
        pre = [1]*size
        suf = [1]*size

        for i in range(1, size):
            pre[i] = (pre[i-1] * arr[i-1]) % 12345

        for i in range(size-2, -1, -1):
            suf[i] = (arr[i+1] * suf[i+1]) % 12345

        res = [(pre[i]*suf[i]) % 12345 for i in range(size)]

        ans = [[0]*n for _ in range(m)]
        idx = 0
        for i in range(m):
            for j in range(n):
                ans[i][j] = res[idx]
                idx += 1

        return ans