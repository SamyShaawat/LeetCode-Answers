class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff = -1 
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    diff = max(diff, nums[j] - nums[i])
                else:
                    break
        return diff 