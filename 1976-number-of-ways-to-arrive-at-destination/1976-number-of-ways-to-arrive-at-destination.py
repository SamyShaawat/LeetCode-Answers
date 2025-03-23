class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7
        INF = 10**20 
        adj_list = defaultdict(list)
        for u,v,w in roads:
           adj_list[u].append((v,w))
           adj_list[v].append((u,w))
        



        count = [0] * n
        best = [INF] * n
        used = [False] * n
        h= []
        heapq.heappush(h, (0,0))
        best[0] = 0
        count[0] = 1
        while len(h) > 0:
            d, node = heapq.heappop(h)
            if used[node]:
                continue
            used[node] = True
            for v, w in adj_list[node]:
                if best[v] > best[node] + w: 
                    best[v] = best[node] + w
                    count[v] = count[node]
                    heapq.heappush(h, (best[v], v))
                elif best[v] == best[node] + w:
                    count[v] += count[node]


        return count[n-1]%mod

        