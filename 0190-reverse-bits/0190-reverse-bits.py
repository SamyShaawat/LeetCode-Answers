class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = bin(n)[2:].zfill(32)
        reverse_str = binary_str[::-1]
        print(reverse_str)
        return int(reverse_str,2)
        