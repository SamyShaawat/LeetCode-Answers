class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((w, v))
            adj[v].append((w<<1, u))

        dist=[0]+[inf]*(n-1)
        pq=[(0, 0)]
        heapq.heapify(pq)

        while pq:
            d, u=heapq.heappop(pq)

            if d>dist[u]: continue
            if u==n-1: return d

            for w, v in adj[u]:
                d2=d+w
                if d2<dist[v]:
                    dist[v]=d2
                    heapq.heappush(pq, (d2, v))
        return -1