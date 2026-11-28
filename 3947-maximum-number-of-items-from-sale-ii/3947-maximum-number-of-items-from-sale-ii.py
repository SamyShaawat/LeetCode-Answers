class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        cnt = [0] * (n + 1)
        for f, _ in items:
            cnt[f] += 1
        D = [0] * (n + 1)
        for v in range(1, n + 1):
            if cnt[v]:
                D[v] = sum(cnt[v::v])
        m = min(p for _, p in items)
        lim = m + m
        groups = sorted([(p, D[f] - 1) for f, p in items if D[f] > 1 and p <= lim])
        t = 0
        R = budget
        for c, k in groups:
            x = R // c
            if x < k:
                t += x
                R -= x * c
                break
            t += k
            R -= k * c
        return 2 * t + R // m
