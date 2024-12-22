class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            j = i+1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result
                j+=1
        