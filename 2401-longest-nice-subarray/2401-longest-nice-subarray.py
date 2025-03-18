class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res =0 
        l = 0
        curr = 0
        n = len(nums)
        for r in range(n):
            while (curr& nums[r])>0:
                curr ^= nums[l]
                l +=1
            curr |= nums[r]
            res = max(res, r-l+1)
        return res