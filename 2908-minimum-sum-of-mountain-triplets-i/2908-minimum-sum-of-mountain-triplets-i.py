class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        inf = 10 ** 20 
        best = inf

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] < nums[j] and nums[j] > nums[k]:
                        best = min(best, nums[i]+nums[j]+nums[k])
        if best >= inf:
            return -1
        return best