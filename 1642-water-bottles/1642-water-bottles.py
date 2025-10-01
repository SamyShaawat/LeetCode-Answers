class Solution:
    def numWaterBottles(self, b: int, n: int) -> int:
        return b + (b - 1) // (n - 1)