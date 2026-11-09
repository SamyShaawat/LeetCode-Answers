from heapq import heappush, heappop, heapreplace

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        n = len(arrival)
        if k >= n:
            return list(range(n))
        free = list(range(k))
        busy = []
        cnt = [0] * k
        push = heappush
        pop = heappop
        rep = heapreplace
        i = 0
        for a, l in zip(arrival, load):
            lim = (a + 1) << 17
            while busy and busy[0] < lim:
                s = pop(busy) & 131071
                push(free, i + (s - i) % k)
            if free:
                while free[0] < i:
                    v = free[0]
                    rep(free, v + ((i - v + k - 1) // k) * k)
                s = pop(free) % k
                cnt[s] += 1
                push(busy, ((a + l) << 17) | s)
            i += 1
        m = max(cnt)
        return [i for i in range(k) if cnt[i] == m]
