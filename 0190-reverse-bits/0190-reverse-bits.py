class Solution:
    def reverseBits(self, n: int) -> int:
        # Convert the integer `n` to a 32-bit binary string.
        # bin(n) returns a string like '0b101', so we remove the '0b' prefix with [2:]
        # zfill(32) ensures it's exactly 32 bits by padding with leading zeros if needed
        binary_str = bin(n)[2:].zfill(32)

        # Reverse the binary string to simulate reversing the bits
        reverse_str = binary_str[::-1]

        # For debugging: print the reversed binary string
        print(reverse_str)

        # Convert the reversed binary string back to an integer (base 2)
        return int(reverse_str, 2)

        