from collections import deque, defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        dp = [[0] * 26 for _ in range(n)]
        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
            dp[i][ord(colors[i]) - ord('a')] = 1

        visited = 0
        maxColor = 0

        while queue:
            node = queue.popleft()
            visited += 1

            for neighbor in adj[node]:
                for c in range(26):
                    inc = 1 if ord(colors[neighbor]) - ord('a') == c else 0
                    dp[neighbor][c] = max(dp[neighbor][c], dp[node][c] + inc)

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

            maxColor = max(maxColor, max(dp[node]))

        return maxColor if visited == n else -1