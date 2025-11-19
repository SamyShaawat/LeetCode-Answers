class Solution:
    def findFinalValue(self, nums: list[int], k: int) -> int:
        bits = 0
        for num in nums:
            if num % k != 0:
                continue
            n = num // k
            if n & (n - 1) == 0:
                bits |= n
        d = bits + 1
        return k * (d & -d)