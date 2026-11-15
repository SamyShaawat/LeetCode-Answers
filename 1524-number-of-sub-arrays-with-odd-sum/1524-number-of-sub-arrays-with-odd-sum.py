from itertools import accumulate

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = sum(map((1).__and__, accumulate(arr)))
        return odd * (len(arr) + 1 - odd) % 1000000007
