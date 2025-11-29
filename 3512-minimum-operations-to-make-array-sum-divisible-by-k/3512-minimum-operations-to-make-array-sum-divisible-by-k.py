class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        ops = total % k
        return ops