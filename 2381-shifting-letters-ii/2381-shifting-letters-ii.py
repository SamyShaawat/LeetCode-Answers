class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)  # Get the length of the input string
        
        diff = [0] * n  # Create a difference array for range updates (same length as s)

        # Populate the difference array based on the shifts
        for start, end, direction in shifts:
            delta = 1 if direction == 1 else -1  # Direction 1 means forward shift, 0 means backward (-1)
            diff[start] += delta  # Apply delta at start index
            if end + 1 < n:
                diff[end + 1] -= delta  # Revert the delta after the end index (range update technique)

        # Compute prefix sum to get the final shift value at each position
        for i in range(1, n):
            diff[i] += diff[i - 1]  # Cumulative sum to apply all previous shifts

        # Apply the calculated shifts to each character
        result = []
        for i, char in enumerate(s):
            shift = diff[i] % 26  # Modulo 26 to handle wrap-around in alphabet
            # Shift the character by shift positions and wrap around using modulo
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))

        return ''.join(result)  # Join the shifted characters to form the final string
