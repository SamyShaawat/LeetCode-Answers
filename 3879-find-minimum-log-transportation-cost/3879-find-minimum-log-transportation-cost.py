class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        min_total_cost = float('inf')

        if n <= k and m <= k:
            min_total_cost = min(min_total_cost, 0)

        if n <= k and m > k and m <= 2 * k:
            cost_m_cut = k * (m - k)
            min_total_cost = min(min_total_cost, cost_m_cut)

        if m <= k and n > k and n <= 2 * k:
            cost_n_cut = k * (n - k)
            min_total_cost = min(min_total_cost, cost_n_cut)

        return min_total_cost