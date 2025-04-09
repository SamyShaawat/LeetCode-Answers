class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR the two numbers.
        # The result will have 1s in the positions where x and y have different bits.
        # Example: x = 4 (0100), y = 1 (0001), x ^ y = 0101 → two differing bits

        # Convert the XOR result to binary and count the number of '1's,
        # which equals the number of differing bits.
        return bin(x ^ y).count('1')
