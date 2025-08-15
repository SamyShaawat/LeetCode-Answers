class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0 
        while (4**(i+1))<=n:
            i+=1
        while i >= 0 :
            power = 4 ** i 
            if power == n :
                return True
            i-=1
        return False