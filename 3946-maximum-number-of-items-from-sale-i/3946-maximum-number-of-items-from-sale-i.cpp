class Solution {
public:
    int maximumSaleItems(vector<vector<int>>& items, int budget) {
        int M = 0, pmin = INT_MAX;
        for (auto& it : items) { M = max(M, it[0]); pmin = min(pmin, it[1]); }
        vector<int> freq(M + 1, 0), cnt(M + 1, 0);
        for (auto& it : items) freq[it[0]]++;
        for (int f = 1; f <= M; f++)
            if (freq[f])
                for (int m = f; m <= M; m += f) cnt[f] += freq[m];
        vector<int> dp(budget + 1, 0);
        for (auto& it : items) {
            int p = it[1], v = cnt[it[0]];
            if (p > budget || v <= p / pmin) continue;
            for (int b = budget; b >= p; b--) dp[b] = max(dp[b], dp[b - p] + v);
        }
        int ans = 0;
        for (int b = 0; b <= budget; b++) ans = max(ans, dp[b] + (budget - b) / pmin);
        return ans;
    }
};