class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        cur = [1 << (ord(c) - 97) for c in s]
        par = [-1] * n
        pre = [0] * n
        dep = [0] * n
        tin = [0] * n
        pre[0] = cur[0]
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            tin[u] = len(order)
            order.append(u)
            pu = pre[u]
            du = dep[u] + 1
            for w in adj[u]:
                if w != par[u]:
                    par[w] = u
                    dep[w] = du
                    pre[w] = pu ^ cur[w]
                    stack.append(w)
        sz = [1] * n
        for i in range(n - 1, 0, -1):
            u = order[i]
            sz[par[u]] += sz[u]
        sp = [[(dep[u] << 16) | par[u] for u in order]]
        j = 1
        while 2 * j <= n:
            p = sp[-1]
            sp.append(list(map(min, p, p[j:])))
            j *= 2
        bit = [0] * (n + 2)
        ans = []
        for q in queries:
            t, a, b = q.split()
            u = int(a)
            if t == "update":
                c = 1 << (ord(b) - 97)
                d = cur[u] ^ c
                if d:
                    cur[u] = c
                    i = tin[u] + 1
                    while i <= n:
                        bit[i] ^= d
                        i += i & -i
                    i = tin[u] + sz[u] + 1
                    while i <= n:
                        bit[i] ^= d
                        i += i & -i
            else:
                v = int(b)
                x = pre[u] ^ pre[v]
                i = tin[u] + 1
                while i:
                    x ^= bit[i]
                    i &= i - 1
                i = tin[v] + 1
                while i:
                    x ^= bit[i]
                    i &= i - 1
                lo = tin[u]
                hi = tin[v]
                if lo > hi:
                    lo, hi = hi, lo
                if lo == hi:
                    l = u
                else:
                    lo += 1
                    k = (hi - lo + 1).bit_length() - 1
                    r = sp[k]
                    y = r[lo]
                    z = r[hi - (1 << k) + 1]
                    l = (y if y < z else z) & 65535
                x ^= cur[l]
                ans.append(x & (x - 1) == 0)
        return ans
