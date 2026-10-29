class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        a = [1 << (ord(c) - 97) for c in s]
        tin = [0] * n
        tout = [0] * n
        base = [0] * n
        order = [0] * n
        up = [0] * n
        up[0] = -1
        base[0] = a[0]
        stack = [0]
        t = 0
        while stack:
            u = stack.pop()
            if u >= 0:
                t += 1
                tin[u] = t
                order[t - 1] = u
                stack.append(~u)
                p = up[u]
                for v in adj[u]:
                    if v != p:
                        up[v] = u
                        base[v] = base[u] ^ a[v]
                        stack.append(v)
            else:
                tout[~u] = t
        # sparse table over dfs order: min tin of parent
        row = [tin[up[order[i]]] if i else 0 for i in range(n)]
        table = [row]
        j = 1
        while (1 << j) <= n:
            h = 1 << (j - 1)
            row = [min(x, y) for x, y in zip(row, row[h:])]
            table.append(row)
            j += 1
        bit = [0] * (n + 2)
        size = n + 1

        def lca(u, v):
            l, r = tin[u], tin[v]
            if l > r:
                l, r = r, l
            if l == r:
                return u
            k = (r - l).bit_length() - 1
            tb = table[k]
            return order[min(tb[l], tb[r - (1 << k)]) - 1]

        ans = []
        for q in queries:
            p = q.split()
            if p[0] == "update":
                u = int(p[1])
                m = a[u] ^ (1 << (ord(p[2]) - 97))
                if m:
                    a[u] ^= m
                    i = tin[u]
                    while i <= size:
                        bit[i] ^= m
                        i += i & -i
                    i = tout[u] + 1
                    while i <= size:
                        bit[i] ^= m
                        i += i & -i
            else:
                u = int(p[1])
                v = int(p[2])
                w = lca(u, v)
                m = base[u] ^ base[v] ^ a[w]
                i = tin[u]
                while i:
                    m ^= bit[i]
                    i &= i - 1
                i = tin[v]
                while i:
                    m ^= bit[i]
                    i &= i - 1
                ans.append(m & (m - 1) == 0)
        return ans
