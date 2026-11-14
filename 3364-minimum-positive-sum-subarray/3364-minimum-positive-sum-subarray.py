from itertools import accumulate

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        p = [0, *accumulate(nums)]
        best = 1000000000
        for i in range(l, len(p)):
            pi = p[i]
            for q in p[max(0, i - r):i - l + 1]:
                s = pi - q
                if 0 < s < best:
                    best = s
        return -1 if best == 1000000000 else best
