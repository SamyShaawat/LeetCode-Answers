class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
    # Bottom Up 
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * (n + 1) for _ in range (m + 1)]
        for i in range (m + 1):
            dp[i][n] = float('-inf')
        for i in range (n + 1):
            dp[m][i] = float('-inf')
        for i in range (m - 1, -1, -1):
            for j in range (n - 1, -1, -1):
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1],
                               nums1[i] * nums2[j] + max(dp[i + 1][j + 1], 0)
                            )
        return dp[0][0]


    # Top Down 
        cache = {}
        def dfs(i, j):
            if i == len(nums1) or j == len(nums2):
                return float('-inf')
            if (i, j) in cache:
                return cache[(i, j)]
            skip_i = dfs(i + 1, j)
            skip_j = dfs(i, j + 1)
            not_skip = nums1[i] * nums2[j] + max(dfs(i + 1, j + 1), 0)
            cache[(i, j)] = max(skip_i, skip_j, not_skip)
            return cache[(i, j)]
        return dfs(0, 0)
            
            
                