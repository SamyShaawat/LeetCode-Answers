from sortedcontainers import SortedList
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = list(range(c + 1))
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        for u, v in connections:
            union(u, v)

        groups = defaultdict(list)
        for station in range(1, c + 1):
            root = find(station)
            groups[root].append(station)

        online = [True] * (c + 1)
        group_online = {}
        for root, stations in groups.items():
            group_online[root] = SortedList(stations)

        res = []
        for qtype, x in queries:
            root = find(x)
            if qtype == 1:
                if online[x]:
                    res.append(x)
                else:
                    sl = group_online[root]
                    if sl:
                        res.append(sl[0])
                    else:
                        res.append(-1)
            else:
                if online[x]:
                    online[x] = False
                    group_online[root].remove(x)

        return res