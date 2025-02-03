class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        cur = 1
        res = 1
        increasing = 0
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                if increasing > 0:
                    cur += 1
                else:
                    cur = 2 
                    increasing = 1

            elif nums[i-1] > nums[i]:
                if increasing < 0:
                    cur += 1
                else:
                    cur = 2 
                    increasing = -1
            else:
                cur = 1 
                increasing = 0 

            res = max(res, cur)
        return res