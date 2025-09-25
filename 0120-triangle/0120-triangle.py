class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:
        for i in range(len(tri) - 2, -1, -1):
            for j in range(len(tri[i])):
                tri[i][j] += min(tri[i + 1][j], tri[i + 1][j + 1])
        return tri[0][0]