# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.


# You can return the answer in any order.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums) 
        for i in range(size):
            for j in range(i+1, size):
                if nums[i] + nums[j] == target:
                    return [i,j]


obj = Solution()
nums = [2, 7, 11, 15]
target = 17
print(obj.twoSum(nums, target))
