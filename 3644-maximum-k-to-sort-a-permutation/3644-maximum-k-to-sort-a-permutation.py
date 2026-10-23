from functools import reduce
from itertools import compress
from operator import and_, ne


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = reduce(and_, compress(nums, map(ne, nums, range(len(nums)))), -1)
        return k if k > 0 else 0
