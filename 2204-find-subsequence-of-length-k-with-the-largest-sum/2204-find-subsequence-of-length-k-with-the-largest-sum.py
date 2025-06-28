class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        for i in range(n-k): nums.remove(min(nums))
        return nums
        