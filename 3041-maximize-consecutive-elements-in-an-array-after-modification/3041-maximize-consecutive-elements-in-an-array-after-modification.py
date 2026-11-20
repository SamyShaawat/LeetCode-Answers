class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        g = dp.get
        for x in nums:
            dp[x + 1] = g(x, 0) + 1
            dp[x] = g(x - 1, 0) + 1
        return max(dp.values())
