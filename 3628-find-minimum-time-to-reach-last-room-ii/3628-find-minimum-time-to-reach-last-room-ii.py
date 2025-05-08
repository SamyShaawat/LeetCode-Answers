class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        output = [[10 ** 11] * m for _ in range(n)]
        output[0][0] = moveTime[0][0]
        q = []
        heapq.heappush(q, (0, 0, 0, 0))
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while q:
            d, i, j, p = heapq.heappop(q)
            if output[i][j] < d:
                continue
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= nj < m and 0 <= ni < n and output[ni][nj] > max(d, moveTime[ni][nj]) + (p + 1):
                    output[ni][nj] = max(moveTime[ni][nj], d) + (p + 1)
                    heapq.heappush(q, (output[ni][nj], ni, nj, (p + 1) % 2))
        return output[n - 1][m - 1]