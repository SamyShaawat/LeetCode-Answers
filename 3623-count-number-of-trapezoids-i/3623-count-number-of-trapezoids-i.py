class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        mp = {}
        for x, y in points:
            mp[y] = mp.get(y, 0) + 1
        seg = []
        for k in mp.values():
            if k >= 2:
                seg.append((k * (k - 1) // 2) % MOD)
        s = 0
        ans = 0
        for v in seg:
            ans = (ans + v * s) % MOD
            s = (s + v) % MOD
        return ans