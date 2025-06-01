class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        num_rows, num_cols = len(mat), len(mat[0])
        row_count, col_count = [0] * num_rows, [0] * num_cols
        num_to_pos = {}

        # Create a map to store the position of each number in the matrix
        for row in range(num_rows):
            for col in range(num_cols):
                num_to_pos[mat[row][col]] = [row, col]

        for i in range(len(arr)):
            num = arr[i]
            row, col = num_to_pos[num]

            # Increment the count for the corresponding row and column
            row_count[row] += 1
            col_count[col] += 1

            # Check if the row or column is completely painted
            if row_count[row] == num_cols or col_count[col] == num_rows:
                return i

        # This line will never be reached as per the problem statement
        return -1