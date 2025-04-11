class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high+1):
            s = str(i)
            n = len(s)
            if n % 2 == 0:
                if sum(int(s[i]) for i in range(n//2)) == sum(int(s[i]) for i in range(n//2, n)):
                    count +=1
                
            else:
                continue
        return count