class Solution:
    def binaryGap(self, n: int) -> int:
        longest_dist = 0
        i = 0
        one_position = 32
        while n:
            if n & 1:
                longest_dist = i - one_position if i - one_position > longest_dist else longest_dist
                one_position = i
            i += 1
            n >>= 1
        return longest_dist