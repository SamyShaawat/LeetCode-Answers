class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda l: l[1])
        order = sorted(range(len(queries)), key=queries.__getitem__)
        cnt = [0] * (n + 1)
        res = [0] * len(queries)
        m = len(logs)
        lo = hi = active = 0
        for qi in order:
            q = queries[qi]
            left = q - x
            while hi < m and logs[hi][1] <= q:
                s = logs[hi][0]
                if cnt[s] == 0:
                    active += 1
                cnt[s] += 1
                hi += 1
            while lo < hi and logs[lo][1] < left:
                s = logs[lo][0]
                cnt[s] -= 1
                if cnt[s] == 0:
                    active -= 1
                lo += 1
            res[qi] = n - active
        return res
