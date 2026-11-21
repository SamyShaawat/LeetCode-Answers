class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        ch = [[] for _ in range(n)]
        for i in range(1, n):
            ch[parent[i]].append(i)
        idx = [ord(c) - 97 for c in s]
        last = [-1] * 26
        np = parent[:]
        saved = [-1] * n
        order = []
        push = order.append
        st = [0]
        pop = st.pop
        app = st.append
        ext = st.extend
        while st:
            u = pop()
            if u >= 0:
                c = idx[u]
                p = last[c]
                if p >= 0:
                    np[u] = p
                push(u)
                kids = ch[u]
                if kids:
                    saved[u] = p
                    last[c] = u
                    app(~u)
                    ext(kids)
            else:
                u = ~u
                last[idx[u]] = saved[u]
        sz = [1] * n
        for u in reversed(order):
            p = np[u]
            if p >= 0:
                sz[p] += sz[u]
        return sz