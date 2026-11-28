class Solution {
    public int maximumSaleItems(int[][] items, int budget) {
        int n = items.length;
        int[] cnt = new int[n + 1];
        int[] D = new int[n + 1];
        long m = Long.MAX_VALUE;
        for (int[] it : items) {
            cnt[it[0]]++;
            m = Math.min(m, it[1]);
        }
        for (int v = 1; v <= n; v++) {
            if (cnt[v] == 0) continue;
            int s = 0;
            for (int w = v; w <= n; w += v) s += cnt[w];
            D[v] = s - 1;
        }
        long lim = 2 * m;
        long[] keys = new long[n];
        int g = 0;
        for (int[] it : items)
            if (it[1] <= lim && D[it[0]] > 0) keys[g++] = ((long) it[1] << 17) | D[it[0]];
        java.util.Arrays.sort(keys, 0, g);
        long t = 0, R = budget;
        for (int i = 0; i < g; i++) {
            long c = keys[i] >>> 17;
            long k = keys[i] & 131071;
            long x = R / c;
            if (x < k) {
                t += x;
                R -= x * c;
                break;
            }
            t += k;
            R -= k * c;
        }
        return (int) (2 * t + R / m);
    }
}
