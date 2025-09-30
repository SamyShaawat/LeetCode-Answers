from math import comb

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for i in range(n):
            result = (result + comb(n - 1, i) * nums[i]) % 10
            
        return result