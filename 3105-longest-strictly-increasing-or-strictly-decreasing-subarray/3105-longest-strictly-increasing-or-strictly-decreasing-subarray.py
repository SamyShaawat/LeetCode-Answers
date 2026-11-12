class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        best = inc = dec = 1
        p = nums[0]
        for x in nums:
            if x > p:
                inc += 1
                dec = 1
            elif x < p:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            if inc > best:
                best = inc
            if dec > best:
                best = dec
            p = x
        return best
