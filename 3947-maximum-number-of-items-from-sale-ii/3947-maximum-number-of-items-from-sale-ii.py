class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        fs, ps = zip(*items)
        cnt = [0] * (len(fs) + 1)
        for f in fs:
            cnt[f] += 1
        D = {v: sum(cnt[v::v]) - 1 for v in set(fs)}
        m = min(ps)
        lim = m + m
        groups = sorted([(p, D[f]) for f, p in items if p <= lim and D[f]])
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
