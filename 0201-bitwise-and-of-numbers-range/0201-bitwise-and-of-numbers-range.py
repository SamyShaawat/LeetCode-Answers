class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while (right > left):  
            right = right & (right - 1) # Clear the least significant bit of right
        return right & left 
# left = 5   -> 0101
# right = 7  -> 0111

# First iteration:
# right = 0111
# right - 1 = 0110
# right & (right - 1) = 0110

# Second iteration:
# right = 0110
# right - 1 = 0101
# right & (right - 1) = 0100

# Now right = 0100, which is less than left = 0101
# Exit loop

# Final AND:
# left  = 0101
# right = 0100
# left & right = 0100 -> 4

        