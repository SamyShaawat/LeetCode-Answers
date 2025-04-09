class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # Convert the number to a string, reverse it, then convert back to int to remove any leading zeros
        # For example: num = 120 → str(num)[::-1] = '021' → int('021') = 21

        # Then, convert the reversed-and-stripped number back to a string and reverse it again
        # Finally, compare it with the original number (converted to string)

        return str(num) == str(int(str(num)[::-1]))[::-1]

        