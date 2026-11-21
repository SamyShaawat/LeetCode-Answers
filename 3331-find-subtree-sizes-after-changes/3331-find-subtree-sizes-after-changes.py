class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        ch = [[] for _ in range(n)]
        for i in range(1, n):
            ch[parent[i]].append(i)
        idx = [ord(c) - 97 for c in s]
        np = parent[:]
        tab = [None] * n
        t0 = [-1] * 26
        t0[idx[0]] = 0
        tab[0] = t0
        order = [0]
        ext = order.extend
        for u in order:
            kids = ch[u]
            if not kids:
                continue
            tu = tab[u]
            for v in kids:
                c = idx[v]
                p = tu[c]
                if p >= 0:
                    np[v] = p
                if ch[v]:
                    t = tu[:]
                    t[c] = v
                    tab[v] = t
            ext(kids)
        sz = [1] * n
        for u in reversed(order):
            p = np[u]
            if p >= 0:
                sz[p] += sz[u]
        return sz