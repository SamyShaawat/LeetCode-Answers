class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curSum = nums[0]
        res = curSum

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                curSum += nums[i]
            else:
                curSum = nums[i]
            res = max(res, curSum)
        return res