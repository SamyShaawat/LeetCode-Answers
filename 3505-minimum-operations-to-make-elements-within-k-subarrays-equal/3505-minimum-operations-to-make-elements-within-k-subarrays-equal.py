from heapq import heappush, heappop
import numpy as np

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        lo = []
        hi = []
        dl = {}
        ls = hs = lc = hc = 0
        c = []
        ap = c.append
        for i in range(n):
            v = nums[i]
            if lo and v <= -lo[0]:
                heappush(lo, -v); ls += v; lc += 1
            else:
                heappush(hi, v); hs += v; hc += 1
            if i >= x:
                u = nums[i - x]
                dl[u] = dl.get(u, 0) + 1
                if u <= -lo[0]:
                    lc -= 1; ls -= u
                else:
                    hc -= 1; hs -= u
                while lo and dl.get(-lo[0], 0) > 0:
                    dl[-lo[0]] -= 1; heappop(lo)
                while hi and dl.get(hi[0], 0) > 0:
                    dl[hi[0]] -= 1; heappop(hi)
            while lc > hc + 1:
                t = -heappop(lo); lc -= 1; ls -= t
                heappush(hi, t); hc += 1; hs += t
                while lo and dl.get(-lo[0], 0) > 0:
                    dl[-lo[0]] -= 1; heappop(lo)
            while lc < hc:
                t = heappop(hi); hc -= 1; hs -= t
                heappush(lo, -t); lc += 1; ls += t
                while hi and dl.get(hi[0], 0) > 0:
                    dl[hi[0]] -= 1; heappop(hi)
            if i >= x - 1:
                m = -lo[0]
                ap(m * lc - ls + hs - m * hc)
        c = np.array(c, dtype=np.int64)
        INF = 1 << 60
        prev = np.zeros(n + 1, dtype=np.int64)
        for j in range(1, k + 1):
            cur = np.full(n + 1, INF, dtype=np.int64)
            s = j * x
            cur[s:] = np.minimum.accumulate(prev[s - x:n + 1 - x] + c[s - x:n + 1 - x])
            prev = cur
        return int(prev[n])
