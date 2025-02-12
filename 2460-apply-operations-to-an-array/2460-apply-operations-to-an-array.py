class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] *=2 
                nums[i] = 0
        l = 0 
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
        return nums
