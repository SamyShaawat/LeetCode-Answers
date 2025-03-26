class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [''] * numRows
        print(rows)
        k = 0
        direction = (numRows == 1) - 1
        print(direction)
        for c in s:
            rows[k] += c
            if k == 0 or k == numRows - 1:
                direction *= -1
                print(direction)
            k += direction
        return ''.join(rows)