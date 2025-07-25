class Solution:
    def maxSum(self, nums: List[int]) -> int:
        total_sum = 0
         
        for num in set(nums):
            print(num) 
            if num > 0: 
                total_sum += num
        if total_sum == 0:
            return max(nums)
        return total_sum