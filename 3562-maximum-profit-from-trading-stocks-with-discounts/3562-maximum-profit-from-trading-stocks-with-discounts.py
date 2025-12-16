class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        tree = [[] for _ in range(n)]
        in_degree = [0] * n
        for u, v in hierarchy:
            u -= 1
            v -= 1
            tree[u].append(v)
            in_degree[v] += 1

        root = 0
        for i in range(n):
            if in_degree[i] == 0:
                root = i
                break

        INF = -10 ** 15

        capability = [0] * n
        def cap(u):
            s = present[u]
            for v in tree[u]:
                s += cap(v)
            capability[u] = min(budget, s)
            return s
        cap(root)
        
        dp0 = [None] * n
        dp1 = [None] * n

        def merge(a, b):
            len_a = len(a) - 1
            len_b = len(b) - 1
            total = min(budget, len_a + len_b)
            c = [INF] * (total + 1)
            for i in range(min(len_a, total) + 1):
                ai = a[i]
                if ai == INF:
                    continue
                maxj = min(len_b, total - i)
                for j in range(maxj + 1):
                    bj = b[j]
                    if bj == INF:
                        continue
                    val = ai + bj
                    if val > c[i + j]:
                        c[i + j] = val
            return c
        def dfs(u):
            for v in tree[u]:
                dfs(v)
            skip = [INF] * (capability[u] + 1)
            skip[0] = 0
            base = [INF] * (capability[u] + 1)
            base[0] = 0
            for v in tree[u]:
                skip = merge(skip, dp0[v])
                base = merge(base, dp1[v])

            def comp(p):
                price = present[u] // 2 if p else present[u]
                profit = future[u] - price
                maximize = skip[:]
                if price <= capability[u]:
                    for b in range(price, capability[u] + 1):
                        if base[b - price] != INF:
                            can = base[b - price] + profit
                            if can > maximize[b]:
                                maximize[b] = can
                return maximize
            dp0[u] = comp(0)
            dp1[u] = comp(1)
        dfs(root)
        return max(dp0[root])
