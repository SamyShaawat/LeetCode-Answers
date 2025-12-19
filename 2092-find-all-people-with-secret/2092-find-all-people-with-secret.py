class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        g = defaultdict(list)
        for x, y, t in meetings:
            g[x].append((y, t))
            g[y].append((x, t))

        inf = 10**18
        time = [inf] * n
        time[0] = time[firstPerson] = 0
        h = [(0, 0), (0, firstPerson)]

        while h:
            t, u = heapq.heappop(h)
            if t > time[u]:
                continue
            for v, mt in g[u]:
                if mt >= t and mt < time[v]:
                    time[v] = mt
                    heapq.heappush(h, (mt, v))

        return [i for i in range(n) if time[i] < inf]