class Solution:
    def setZeroes(self, matrix):
        zero_pos = []
        m, n = len(matrix), len(matrix[0])

        # Record zero positions
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_pos.append((i, j))

        # Apply zeroing
        for row, col in zero_pos:
            self.make_row_zero(matrix[row])
            self.make_column_zero(matrix, col)

    def make_row_zero(self, row):
        for i in range(len(row)):
            row[i] = 0

    def make_column_zero(self, matrix, col_index):
        for row in matrix:
            row[col_index] = 0