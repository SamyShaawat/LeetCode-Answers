class Solution {
    public int maximumSaleItems(int[][] items, int budget) {
        int M = 0, pmin = Integer.MAX_VALUE;
        for (int[] it : items) { M = Math.max(M, it[0]); pmin = Math.min(pmin, it[1]); }
        int[] freq = new int[M + 1], cnt = new int[M + 1];
        for (int[] it : items) freq[it[0]]++;
        for (int f = 1; f <= M; f++)
            if (freq[f] > 0)
                for (int m = f; m <= M; m += f) cnt[f] += freq[m];
        int[] dp = new int[budget + 1];
        for (int[] it : items) {
            int p = it[1], v = cnt[it[0]];
            if (p > budget || v <= p / pmin) continue;
            for (int b = budget; b >= p; b--) dp[b] = Math.max(dp[b], dp[b - p] + v);
        }
        int ans = 0;
        for (int b = 0; b <= budget; b++) ans = Math.max(ans, dp[b] + (budget - b) / pmin);
        return ans;
    }
}