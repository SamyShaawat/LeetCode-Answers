class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return sum(nums[(n + 1) // 2:]) - sum(nums[:n // 2])
