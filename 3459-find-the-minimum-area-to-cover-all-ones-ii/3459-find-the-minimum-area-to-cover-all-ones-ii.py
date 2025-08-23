class Solution:
    def minimumSum(self, A: List[List[int]]) -> int:
        res = float("inf")
        for _ in range(4):
            n, m = len(A), len(A[0])
            for i in range(1, n):
                a1 = self.minimumArea(A[:i])
                for j in range(1, m):
                    part2 = [row[:j] for row in A[i:]]
                    part3 = [row[j:] for row in A[i:]]
                    a2 = self.minimumArea(part2)
                    a3 = self.minimumArea(part3)
                    res = min(res, a1 + a2 + a3)
                for i2 in range(i + 1, n):
                    part2 = A[i:i2]
                    part3 = A[i2:]
                    a2 = self.minimumArea(part2)
                    a3 = self.minimumArea(part3)
                    res = min(res, a1 + a2 + a3)
            A = self.rotate(A)
        return res

    def minimumArea(self, A: List[List[int]]) -> int:
        if not A or not A[0]:
            return 0
        n, m = len(A), len(A[0])
        left, top, right, bottom = float("inf"), float("inf"), -1, -1
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    left = min(left, j)
                    top = min(top, i)
                    right = max(right, j)
                    bottom = max(bottom, i)
        if right == -1:
            return 0
        return (right - left + 1) * (bottom - top + 1)

    def rotate(self, A: List[List[int]]) -> List[List[int]]:
        n, m = len(A), len(A[0])
        return [[A[i][j] for i in range(n-1, -1, -1)] for j in range(m)]