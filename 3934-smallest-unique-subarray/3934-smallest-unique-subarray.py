class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        M = (1 << 61) - 1
        B = 100003
        H = [0] * (n + 1)
        h = 0
        for i, x in enumerate(nums, 1):
            h = (h * B + x) % M
            H[i] = h
        lo, hi = 1, n
        while lo < hi:
            L = (lo + hi) >> 1
            P = pow(B, L, M)
            cnt = Counter([(H[i + L] - H[i] * P) % M for i in range(n - L + 1)])
            if 1 in cnt.values():
                hi = L
            else:
                lo = L + 1
        return lo
