class Solution {
public:
    int minimumChanges(string s, int k) {
        int n = s.size();
        const int INF = 1e9;
        static int w[200][200];
        for (int e = 0; e < n; e++) for (int p = 0; p < n; p++) w[e][p] = INF;
        for (int d = 1; d <= n / 2; d++) {
            vector<int> pm2(n + 1, 0), pm1(n + 1, 0);
            for (int L = 2 * d; L <= n; L += d) {
                vector<int> cur(n - L + 1, 0);
                for (int i = 0; i + L <= n; i++) {
                    int c = pm2[i + d];
                    for (int r = 0; r < d; r++) c += s[i + r] != s[i + L - d + r];
                    cur[i] = c;
                    if (c < w[i + L - 1][i]) w[i + L - 1][i] = c;
                }
                pm2 = move(pm1);
                pm1 = move(cur);
            }
        }
        vector<int> f(n + 1, INF);
        for (int i = 2; i <= n - 2 * (k - 1); i++) f[i] = w[i - 1][0];
        for (int j = 2; j <= k; j++) {
            vector<int> g(n + 1, INF);
            int lo = 2 * (j - 1);
            for (int i = 2 * j; i <= n - 2 * (k - j); i++) {
                int best = INF;
                for (int p = lo; p <= i - 2; p++) best = min(best, f[p] + w[i - 1][p]);
                g[i] = best;
            }
            f = move(g);
        }
        return f[n];
    }
};
