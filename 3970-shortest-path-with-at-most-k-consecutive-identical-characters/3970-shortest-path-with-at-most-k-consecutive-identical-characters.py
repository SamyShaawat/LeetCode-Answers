from heapq import heappush, heappop


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        K = k + 1
        INF = 1 << 60
        dist = [INF] * (n * K)
        dist[1] = 0
        last = n - 1
        pop = heappop
        push = heappush
        h = [1]
        mask = (1 << 22) - 1
        while h:
            x = pop(h)
            s = x & mask
            d = x >> 22
            if d > dist[s]:
                continue
            u, c = divmod(s, K)
            if u == last:
                return d
            lu = labels[u]
            for v, w in adj[u]:
                nc = c + 1 if labels[v] == lu else 1
                if nc > k:
                    continue
                t = v * K + nc
                nd = d + w
                if nd < dist[t]:
                    dist[t] = nd
                    push(h, (nd << 22) | t)
        return -1
