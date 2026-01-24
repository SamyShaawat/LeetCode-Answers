class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        n = len(nums)
        for i in range(n // 2):
            max_sum = max(max_sum, nums[i] + nums[n - 1 - i])
        return max_sum