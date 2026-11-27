class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        M = max(f for f, _ in items)
        freq = [0] * (M + 1)
        for f, _ in items:
            freq[f] += 1
        cnt = [0] * (M + 1)
        for f in range(1, M + 1):
            if freq[f]:
                cnt[f] = sum(freq[f::f]) - 1
        pmin = min(p for _, p in items)
        dp = [0] * (budget + 1)
        for f, p in items:
            v = cnt[f]
            if v and p <= budget:
                v += 1
                dp[p:] = map(max, dp[p:], [x + v for x in dp[:-p]])
        return max(dp[b] + (budget - b) // pmin for b in range(budget + 1))
