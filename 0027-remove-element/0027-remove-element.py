class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # using two pointers:
        k = 0 # first pointer 
        for i in range(len(nums)): # i is the secongd pointer
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k
# another solution  
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         while val in nums:
#             nums.remove(val)
#         return len(nums)
