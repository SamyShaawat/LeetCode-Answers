from heapq import heappush, heappop, heapreplace

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = list(range(k))
        busy = []
        cnt = [0] * k
        M = 131071
        push = heappush
        pop = heappop
        for i in range(len(arrival)):
            a = arrival[i]
            lim = (a + 1) << 17
            while busy and busy[0] < lim:
                s = pop(busy) & M
                push(free, i + (s - i) % k)
            if free:
                while free[0] < i:
                    v = free[0]
                    heapreplace(free, v + ((i - v + k - 1) // k) * k)
                s = pop(free) % k
                cnt[s] += 1
                push(busy, ((a + load[i]) << 17) | s)
        m = max(cnt)
        return [i for i in range(k) if cnt[i] == m]
