from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = 0
        for x in nums:
            total = (total + x) % p
        
        need = total
        if need == 0:
            return 0
        
        n = len(nums)
        last_index = {0: -1}
        ans = n
        prefix = 0
        
        for i, x in enumerate(nums):
            prefix = (prefix + x) % p
            target = (prefix - need) % p
            
            if target in last_index:
                ans = min(ans, i - last_index[target])
            
            last_index[prefix] = i
        
        return -1 if ans == n else ans