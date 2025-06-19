class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        Min = nums[0]
        for num in nums[1:]:
            if num - Min > k:
                res += 1
                Min = num
        return res