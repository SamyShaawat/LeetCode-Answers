class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        xor = 0
        n = len(nums) - 2

        for num in nums:
            xor ^= num
        for i in range(n):                  
            xor ^= i

        diffBit = xor & -xor

        a = b = 0
        for num in nums:
            if num & diffBit == 0:
                a ^= num
            else:
                b ^= num
        for i in range(n):
            if i & diffBit == 0:
                a ^= i
            else:
                b ^= i

        return [a, b]