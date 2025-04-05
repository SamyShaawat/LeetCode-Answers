class Solution:
    def hammingWeight(self, n: int) -> int:
        # binary_str = bin(n)
        # print(binary_str) # 0b1011
        binary_str = bin(n)[2:]
        # print(binary_str) # 1011

        return binary_str.count('1')
        