from itertools import accumulate
from operator import xor

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = sum(accumulate(map((1).__and__, arr), xor))
        return odd * (len(arr) + 1 - odd) % 1000000007
