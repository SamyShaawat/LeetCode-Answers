class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        
        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            if i == n:
                dp[i][j] = m - j
                return dp[i][j]
            if j == m:
                dp[i][j] = n - i
                return dp[i][j]
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dfs(i + 1, j + 1)
            else:
                dp[i][j] = 1 + min(dfs(i + 1, j), dfs(i, j + 1))
            return dp[i][j]

        dfs(0, 0)

        def build_scs(i, j):
            res = []
            while i < n or j < m:
                if i == n:
                    res.extend(str2[j:])
                    break
                if j == m:
                    res.extend(str1[i:])
                    break
                if str1[i] == str2[j]:
                    res.append(str1[i])
                    i += 1
                    j += 1
                elif dp[i + 1][j] < dp[i][j + 1]:
                    res.append(str1[i])
                    i += 1
                else:
                    res.append(str2[j])
                    j += 1
            return res

        return ''.join(build_scs(0, 0))