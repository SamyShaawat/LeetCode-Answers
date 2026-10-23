class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # only misplaced elements need swaps; k must be a submask of all of them
        k = -1
        for i, x in enumerate(nums):
            if i != x:
                k &= x
        return max(k, 0)
