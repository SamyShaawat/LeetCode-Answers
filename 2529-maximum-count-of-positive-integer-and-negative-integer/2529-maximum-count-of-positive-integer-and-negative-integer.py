class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        pindex = bisect.bisect_left(nums, 1)
        pcount = n - pindex
        nindex = bisect.bisect_left(nums, 0)
        ncount = nindex
        return max(pcount, ncount)
        