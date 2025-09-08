class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check(x):
            return '0' not in str(x)
        print(check(10))
        res = []
        for i in range(1, n+1):
            if check(i) and check(n-i):
                res.append(i)
                res.append(n-i)
                return res