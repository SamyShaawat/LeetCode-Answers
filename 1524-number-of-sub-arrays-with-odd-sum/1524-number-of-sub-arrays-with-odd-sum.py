class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        curr_sum = 0
        even_cnt = 0 
        odd_cnt = 0
        res = 0
        mod = 10**9 + 7

        for num in arr:
            curr_sum += num
            if curr_sum % 2:  # odd
                res = (res + 1 + even_cnt) % mod
                odd_cnt +=1
            else: # even 
                res = (res + odd_cnt) % mod
                even_cnt += 1
        return res
        