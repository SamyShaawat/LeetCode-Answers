class Solution(object):
    def minimumDifference(self, nums: list[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        min_diff = float('inf')
        length = len(nums)

        for i in range(length - k + 1):
            min_diff = min(min_diff, nums[i + k - 1] - nums[i])

        return min_diff