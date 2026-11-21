class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        ch = [[] for _ in range(n)]
        for i in range(1, n):
            ch[parent[i]].append(i)
        last = {}
        np = parent[:]
        order = []
        push = order.append
        st = [0]
        pop = st.pop
        ext = st.extend
        app = st.append
        saved = [-1] * n
        while st:
            u = pop()
            if u >= 0:
                c = s[u]
                p = last.get(c, -1)
                if p >= 0:
                    np[u] = p
                saved[u] = p
                last[c] = u
                push(u)
                app(~u)
                ext(ch[u])
            else:
                u = ~u
                last[s[u]] = saved[u]
        sz = [1] * n
        for u in reversed(order):
            p = np[u]
            if p >= 0:
                sz[p] += sz[u]
        return sz