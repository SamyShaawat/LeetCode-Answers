class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def isGood(nums):
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    return False
            return True

        ops = 0
        
        while not isGood(nums):
            min_sum = float('inf')
            min_index = -1
            
          
            for i in range(len(nums) - 1):
                if nums[i] + nums[i+1] < min_sum:
                    min_sum = nums[i] + nums[i+1]
                    min_index = i
            
           
            nums[min_index] = nums[min_index] + nums[min_index + 1]
            nums.pop(min_index + 1)  
            ops += 1
        
        return ops