from heapq import heapify, heappush, heappop
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        m = n - x + 1
        cost = [0] * m
        h = (x + 1) // 2
        s = sorted(nums[:x])
        lo = [-v for v in s[:h]]
        hi = s[h:]
        heapify(lo)
        heapify(hi)
        ls = sum(s[:h])
        hs = sum(s[h:])
        hl = x - h
        dl = {}
        dh = {}
        gl = dl.get
        gh = dh.get
        for i in range(m):
            med = -lo[0]
            cost[i] = med * h - ls + hs - med * hl
            if i == m - 1:
                break
            v = nums[i + x]
            u = nums[i]
            if v <= med:
                heappush(lo, -v)
                ls += v
                bal = 1
            else:
                heappush(hi, v)
                hs += v
                bal = -1
            if u <= med:
                ls -= u
                bal -= 1
                dl[u] = gl(u, 0) + 1
            else:
                hs -= u
                bal += 1
                dh[u] = gh(u, 0) + 1
            if bal > 0:
                while gl(-lo[0]):
                    dl[-lo[0]] -= 1
                    heappop(lo)
                t = -heappop(lo)
                ls -= t
                hs += t
                heappush(hi, t)
            elif bal < 0:
                while gh(hi[0]):
                    dh[hi[0]] -= 1
                    heappop(hi)
                t = heappop(hi)
                hs -= t
                ls += t
                heappush(lo, -t)
            while lo and gl(-lo[0]):
                dl[-lo[0]] -= 1
                heappop(lo)
            while hi and gh(hi[0]):
                dh[hi[0]] -= 1
                heappop(hi)
        INF = 1 << 60
        prev = [0] * (n + 1)
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            best = INF
            for i in range(j * x, n + 1):
                c = prev[i - x] + cost[i - x]
                if c < best:
                    best = c
                cur[i] = best
            prev = cur
        return prev[n]
