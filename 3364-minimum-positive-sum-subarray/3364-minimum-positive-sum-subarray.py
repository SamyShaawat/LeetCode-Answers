class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + nums[i]
        best = 1 << 30
        for i in range(l, n + 1):
            pi = p[i]
            for j in range(max(0, i - r), i - l + 1):
                s = pi - p[j]
                if 0 < s < best:
                    best = s
        return best if best != 1 << 30 else -1
