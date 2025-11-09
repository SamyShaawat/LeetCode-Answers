class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        def f(x, y, cnt):
            if x==0 or y==0: return cnt
        #    if x<y: return f(y, x, cnt)
            q,r=divmod(x, y)
            return f(y, r, cnt+q)
        return f(num1, num2, 0)
        