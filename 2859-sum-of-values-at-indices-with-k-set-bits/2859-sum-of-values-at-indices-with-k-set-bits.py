class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            if bin(i)[2:].count('1') == k:
                count += nums[i]
        return count
        
        