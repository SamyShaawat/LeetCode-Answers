class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        while n: 
            n, x = divmod(n, k)
            ans += x
        return ans
        