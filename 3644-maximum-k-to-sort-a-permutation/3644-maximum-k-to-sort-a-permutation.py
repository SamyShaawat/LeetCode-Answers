class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1
        for i, x in enumerate(nums):
            if i != x:
                k &= x
                if not k:
                    return 0
        return max(k, 0)
