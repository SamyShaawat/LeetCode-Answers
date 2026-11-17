class Solution {
    public int minimumChanges(String str, int k) {
        char[] s = str.toCharArray();
        int n = s.length;
        final int INF = 1000000000;
        int[][] w = new int[n][n];
        for (int[] row : w) java.util.Arrays.fill(row, INF);
        for (int d = 1; d <= n / 2; d++) {
            int[] pm2 = new int[n + 1], pm1 = new int[n + 1];
            for (int L = 2 * d; L <= n; L += d) {
                int[] cur = new int[n - L + 1];
                for (int i = 0; i + L <= n; i++) {
                    int c = pm2[i + d];
                    for (int r = 0; r < d; r++) if (s[i + r] != s[i + L - d + r]) c++;
                    cur[i] = c;
                    if (c < w[i + L - 1][i]) w[i + L - 1][i] = c;
                }
                pm2 = pm1;
                pm1 = cur;
            }
        }
        int[] f = new int[n + 1];
        java.util.Arrays.fill(f, INF);
        for (int i = 2; i <= n - 2 * (k - 1); i++) f[i] = w[i - 1][0];
        for (int j = 2; j <= k; j++) {
            int[] g = new int[n + 1];
            java.util.Arrays.fill(g, INF);
            int lo = 2 * (j - 1);
            for (int i = 2 * j; i <= n - 2 * (k - j); i++) {
                int best = INF;
                int[] row = w[i - 1];
                for (int p = lo; p <= i - 2; p++) {
                    int v = f[p] + row[p];
                    if (v < best) best = v;
                }
                g[i] = best;
            }
            f = g;
        }
        return f[n];
    }
}
