class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        pref = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pref[i][j] = (
                    mat[i-1][j-1]
                    + pref[i-1][j]
                    + pref[i][j-1]
                    - pref[i-1][j-1]
                )

        maxSide = min(m, n)

        while maxSide > 0:
            for i in range(m - maxSide + 1):
                for j in range(n - maxSide + 1):
                    s = (
                        pref[i+maxSide][j+maxSide]
                        - pref[i][j+maxSide]
                        - pref[i+maxSide][j]
                        + pref[i][j]
                    )
                    if s <= threshold:
                        return maxSide
            maxSide -= 1

        return 0