class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        rowSum = [[0] * (c + 1) for _ in range(r + 1)]
        colSum = [[0] * (c + 1) for _ in range(r + 1)]
        diag = [[0] * (c + 1) for _ in range(r + 1)]
        antidiag = [[0] * (c + 1) for _ in range(r + 1)]

        for i in range(r):
            for j in range(c):
                x = grid[i][j]
                rowSum[i + 1][j + 1] = rowSum[i + 1][j] + x
                colSum[i + 1][j + 1] = colSum[i][j + 1] + x
                diag[i + 1][j + 1] = diag[i][j] + x
                antidiag[i + 1][j] = antidiag[i][j + 1] + x
        def isMagic(k : int) -> bool:
            for i in range(r - k + 1):
                for j in range(c - k + 1):
                    s = diag[i + k][j + k] - diag[i][j]
                    anti = antidiag[i + k][j] - antidiag[i][j + k]
                    if s != anti:
                        continue
                    valid = True
                    for m in range(k):
                        row = rowSum[i + m + 1][j + k] - rowSum[i + m + 1][j]
                        col = colSum[i + k][j + m + 1] - colSum[i][j + m + 1]
                        if row != s or col != s:
                            valid = False
                            break
                    if valid:
                        return True
            return False
        for k in range(min(r, c), 1, -1):
            if isMagic(k):
                return k
        return 1