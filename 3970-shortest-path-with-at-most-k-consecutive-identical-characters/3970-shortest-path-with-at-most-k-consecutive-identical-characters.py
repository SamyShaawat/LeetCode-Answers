from heapq import heappush, heappop


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        K = k + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w, labels[u] == labels[v]))
        last = n - 1
        dist = [1 << 60] * (n * K)
        dist[1] = 0
        minc = [K] * n
        h = [1]
        pop = heappop
        push = heappush
        mask = (1 << 22) - 1
        while h:
            x = pop(h)
            s = x & mask
            d = x >> 22
            if d > dist[s]:
                continue
            u = s // K
            c = s - u * K
            if c >= minc[u]:
                continue
            if u == last:
                return d
            minc[u] = c
            c1 = c + 1
            for v, w, same in adj[u]:
                if same:
                    if c1 >= minc[v]:
                        continue
                    nc = c1
                else:
                    if minc[v] == 1:
                        continue
                    nc = 1
                t = v * K + nc
                nd = d + w
                if nd < dist[t]:
                    dist[t] = nd
                    push(h, (nd << 22) | t)
        return -1
