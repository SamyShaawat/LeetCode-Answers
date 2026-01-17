# As all the points are already sorted, we don't need to sort it explicitly (mentioned in constraints)
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        maxi = 0
        for i in range(n):
            ai, bi = bottomLeft[i]
            ci, di = topRight[i]
            for j in range(i + 1, n):
                aj, bj = bottomLeft[j]
                cj, dj = topRight[j]

                height = min(cj, ci) - max(aj, ai)
                width = min(dj, di) - max(bj, bi)

                maxi = max(maxi, min(height, width))
        return maxi * maxi