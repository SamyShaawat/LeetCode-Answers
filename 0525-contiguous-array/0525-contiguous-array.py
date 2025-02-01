class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero = 0 
        one = 0
        res = 0 
        hash_map = {} # diff -> index 
                      # diff = count of 1's - count of 0's
        for index, n in enumerate(nums):
            if n == 0 :
                zero += 1
            else: 
                one +=1
            diff = one - zero
            if diff not in hash_map:
                hash_map[diff] = index
            if one == zero:
                res = one + zero 
            else:
                lookup_index = hash_map[diff]
                res = max(res, index- lookup_index)

        return res 