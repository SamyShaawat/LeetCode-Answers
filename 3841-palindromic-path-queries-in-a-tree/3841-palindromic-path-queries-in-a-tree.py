class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        val = [1 << (ord(c) - 97) for c in s]
        par = [-1] * n
        dep = [0] * n
        pre = val[:]
        order = [0]
        for v in order:
            p = par[v]
            for w in adj[v]:
                if w != p:
                    par[w] = v
                    dep[w] = dep[v] + 1
                    pre[w] ^= pre[v]
                    order.append(w)
        size = [1] * n
        heavy = [-1] * n
        best = [0] * n
        for v in reversed(order):
            p = par[v]
            if p >= 0:
                size[p] += size[v]
                if size[v] > best[p]:
                    best[p] = size[v]
                    heavy[p] = v
        head = [0] * n
        tin = [0] * n
        stack = [0]
        cnt = 0
        while stack:
            v = stack.pop()
            tin[v] = cnt
            cnt += 1
            h = heavy[v]
            p = par[v]
            for w in adj[v]:
                if w != p and w != h:
                    head[w] = w
                    stack.append(w)
            if h >= 0:
                head[h] = head[v]
                stack.append(h)
        bit = [0] * (n + 2)
        res = []
        for q in queries:
            t, a, b = q.split()
            u = int(a)
            if t == "update":
                d = val[u] ^ (1 << (ord(b) - 97))
                if d:
                    val[u] ^= d
                    i = tin[u] + 1
                    while i <= n:
                        bit[i] ^= d
                        i += i & -i
                    i = tin[u] + size[u] + 1
                    while i <= n:
                        bit[i] ^= d
                        i += i & -i
            else:
                v = int(b)
                x = u
                y = v
                while head[x] != head[y]:
                    if dep[head[x]] > dep[head[y]]:
                        x = par[head[x]]
                    else:
                        y = par[head[y]]
                l = x if dep[x] < dep[y] else y
                m = pre[u] ^ pre[v] ^ val[l]
                i = tin[u] + 1
                while i:
                    m ^= bit[i]
                    i &= i - 1
                i = tin[v] + 1
                while i:
                    m ^= bit[i]
                    i &= i - 1
                res.append(m & (m - 1) == 0)
        return res
