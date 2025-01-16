from operator import xor
from functools import reduce
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # nums3 = []
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         x = nums1[i] ^ nums2[j]
        #         nums3.append(x)
        

        # result = reduce(xor, map(int, nums3))
        # return result

        len1 = len(nums1)
        len2 = len(nums2)
        freq = {}

        for i in nums1:
            freq[i] = freq.get(i,0)+ len2 
        print(freq)
        for j in nums2:
            freq[j] = freq.get(j,0)+ len1 
        print(freq)

        res = 0 
        for key, value in freq.items():
            if value % 2 != 0:
                res ^= key
        return res