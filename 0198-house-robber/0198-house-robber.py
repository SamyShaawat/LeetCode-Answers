class Solution:
    def rob(self, nums: List[int]) -> int:
        low, high, res = 0, 0, 0 
        
        for num in nums:
            cur = low + num
            new_high = max(high, cur) 
            low = high 
            high = new_high
            res = high
        
        return res