from collections import Counter

class Solution:
    def numSplits(self, s: str) -> int:
        # Count characters on the right side initially (whole string)
        right_counter = Counter(s)
        left_counter = Counter()
        good_splits = 0

        # Iterate through each character, moving it from right to left
        for char in s:
            # Add current char to the left side
            left_counter[char] += 1
            # Remove current char from the right side
            right_counter[char] -= 1

            # If no more of this char remain on the right, remove it from the dict
            if right_counter[char] == 0:
                del right_counter[char]

            # Check if number of unique chars are equal on both sides
            if len(left_counter) == len(right_counter):
                good_splits += 1

        return good_splits
