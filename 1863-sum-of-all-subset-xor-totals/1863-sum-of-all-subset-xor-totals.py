class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def helper(i, total):
            if i == len(nums):
                return total
            return helper(i+1, total^nums[i]) + helper(i+1, total)
        return helper(0,0)