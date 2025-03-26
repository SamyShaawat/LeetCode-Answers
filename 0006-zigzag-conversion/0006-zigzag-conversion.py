class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [''] * numRows # list of empty strings to store characters for each row
        # print(rows)
        k = 0 # Index to track the current row

        # Direction of movement (1 for down, -1 for up)
        # If numRows is 1, direction will be 0 (no zigzag needed)
        direction = (numRows == 1) - 1
        # print(direction)
        for c in s:
            rows[k] += c # Append the character to the current row
            # If we reach the first or last row, change direction
            if k == 0 or k == numRows - 1:
                direction *= -1 # Reverse direction
                # print(direction)
            k += direction # Move to the next row in the current direction
        return ''.join(rows)