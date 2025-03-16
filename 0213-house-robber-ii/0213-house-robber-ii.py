class Solution:
    def rob(self, nums: List[int]) -> int:
           
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]

            def robcircle (nums) : 
                prev, curr = 0, 0
                for num in nums:
                     prev , curr = curr , max (curr , prev + num )
                return curr

            return  max(robcircle(nums[1:]), robcircle(nums[:-1]))