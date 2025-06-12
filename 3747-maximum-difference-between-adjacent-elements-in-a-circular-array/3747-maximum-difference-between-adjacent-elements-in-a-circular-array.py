class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res =  float("-inf")
        # print(res)
        for i in range(1, n):
            if i == n-1:
                diff = abs(nums[-1] - nums[0])
                res = max(res, diff)
                # print("last: ",diff)
            diff = abs(nums[i-1] - nums[i])
                # print("loop: ",diff)
            res = max(res, diff)
        
        # print(res)
        return res

        