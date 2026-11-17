from operator import ne, add
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        b = s.encode()
        INF = 10**9
        w = [[INF] * n for _ in range(n)]
        for d in range(1, n // 2 + 1):
            pm2 = [0] * (n + 1)
            pm1 = [0] * (n + 1)
            L = 2 * d
            while L <= n:
                cur = [0] * (n - L + 1)
                for i in range(n - L + 1):
                    c = pm2[i + d] + sum(map(ne, b[i:i + d], b[i + L - d:i + L]))
                    cur[i] = c
                    row = w[i + L - 1]
                    if c < row[i]:
                        row[i] = c
                pm2, pm1 = pm1, cur
                L += d
        f = [INF] * (n + 1)
        for i in range(2, n - 2 * (k - 1) + 1):
            f[i] = w[i - 1][0]
        for j in range(2, k + 1):
            g = [INF] * (n + 1)
            lo = 2 * (j - 1)
            for i in range(2 * j, n - 2 * (k - j) + 1):
                g[i] = min(map(add, f[lo:i - 1], w[i - 1][lo:i - 1]))
            f = g
        return f[n]
