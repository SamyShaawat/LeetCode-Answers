class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return (len(nums) - 1) * (~sum(nums) & 1)