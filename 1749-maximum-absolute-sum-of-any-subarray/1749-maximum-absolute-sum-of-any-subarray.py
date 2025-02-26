class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur = 0
        max_pre, min_pre = 0, 0
        res = 0
        for num in nums:
            cur += num
            res = max(res,max(abs(cur-max_pre), abs(cur-min_pre)))
            max_pre = max(cur, max_pre)
            min_pre = min(cur, min_pre)
        return res