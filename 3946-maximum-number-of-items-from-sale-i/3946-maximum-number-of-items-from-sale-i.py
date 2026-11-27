import numpy as np

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        M = max(f for f, _ in items)
        freq = [0] * (M + 1)
        for f, _ in items:
            freq[f] += 1
        cnt = [0] * (M + 1)
        for f in range(1, M + 1):
            if freq[f]:
                cnt[f] = sum(freq[f::f])
        pmin = min(p for _, p in items)
        dp = np.zeros(budget + 1, dtype=np.int64)
        mx = np.maximum
        for f, p in items:
            v = cnt[f]
            if v > p // pmin and p <= budget:
                mx(dp[p:], dp[:-p] + v, out=dp[p:])
        return int((dp + (budget - np.arange(budget + 1)) // pmin).max())
