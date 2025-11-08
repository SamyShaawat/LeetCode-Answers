class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        while n:
            res ^= n
            n >>= 1
        return res