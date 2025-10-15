class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        up, preUp, res = 1, 0, 0
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up += 1
            else:
                preUp = up
                up = 1
            half = up >> 1
            m = min(preUp, up)
            candidate = max(half, m)
            if candidate > res:
                res = candidate
        return res