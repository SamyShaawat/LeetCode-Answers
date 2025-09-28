class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a = nums[i]
            b = nums[i + 1]
            c = nums[i + 2]
            
            if a < b + c:
                perimeter = a + b + c
                return perimeter
        error = 0 
        return error
        