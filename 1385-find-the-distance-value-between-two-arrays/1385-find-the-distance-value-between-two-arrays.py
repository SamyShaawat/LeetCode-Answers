from bisect import bisect_left


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        b = sorted(arr2)
        n = len(b)
        c = 0
        for x in arr1:
            i = bisect_left(b, x - d)
            if i == n or b[i] > x + d:
                c += 1
        return c
