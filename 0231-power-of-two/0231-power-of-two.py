class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n > 0:
        #     num = bin(n)[2::]
        # else:
        #     num = bin(n)[3::]
        # hashmap = Counter(num)
        # for key, value in hashmap.items():
        #     if n > 0:
        #         if key == '1':
        #             if value == 1:
        #                 return True
        # return False
        i = 0 
        while (2**(i+1) <= n):
            i+=1
        while (i >=0):
            power = 2**i
            if power == n:
                return True
            i-=1
        return False