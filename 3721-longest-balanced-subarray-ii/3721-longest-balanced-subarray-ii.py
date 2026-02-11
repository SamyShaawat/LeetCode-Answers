class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        def ctz(x):
            return (x & -x).bit_length() - 1

        def add(i, v):
            x = i | m
            while x:
                x = (x >> ctz(x)) - 1
                tg[x] += v
            x = i | m
            while x:
                x >>= 1
                mx[x] = max(mx[x << 1] + tg[x << 1], mx[x << 1 | 1] + tg[x << 1 | 1])
                mn[x] = min(mn[x << 1] + tg[x << 1], mn[x << 1 | 1] + tg[x << 1 | 1])

        def q():
            x, d = 1, 0
            while x < m:
                d -= tg[x]
                x <<= 1
                if not mn[x] <= d - tg[x] <= mx[x]:
                    x |= 1
            return x ^ m

        n = len(nums)
        m = 1 << n.bit_length()
        last = [0] * (max(nums) + 1)
        mn = [0] * (m << 1)
        mx = [0] * (m << 1)
        tg = [0] * (m << 1)
        ans = 0
        for i, v in enumerate(nums, 1):
            x = 1 if v & 1 else -1
            if pi := last[v]:
                add(pi, -x)
            add(i, x)
            last[v] = i
            ans = max(ans, i - q())
        return ans