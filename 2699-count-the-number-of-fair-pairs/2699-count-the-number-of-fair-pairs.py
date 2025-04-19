class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        for i,value in enumerate(nums):
            iMin = bisect_left(nums, lower-value, i+1)
            iMax = bisect_right(nums, upper-value, i+1)
            res += (iMax-iMin)
            
        return res