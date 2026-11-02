class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        h = len(nums) // 2
        return sum(nums[-h:]) - sum(nums[:h]) if h else 0
