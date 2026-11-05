from bisect import bisect_left


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        b = sorted(set(arr2))
        b.append(10**9)
        return sum(b[bisect_left(b, x - d)] > x + d for x in arr1)
