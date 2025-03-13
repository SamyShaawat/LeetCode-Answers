class Solution:
    def isHappy(self, n: int) -> bool:
        res = []
        while n != 1:
            n = sum([int(x)**2 for x in str(n)])
            if n in res:
                break
            res.append(n)

        if n == 1 : return True 
        else: return False
