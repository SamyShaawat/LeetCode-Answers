class Solution {
    public long minOperations(int[] nums, int x, int k) {
        int n = nums.length, m = n - x + 1;
        long[] keys = new long[n];
        for (int i = 0; i < n; i++) keys[i] = ((long) (nums[i] + 1000000) << 20) | i;
        Arrays.sort(keys);
        int[] rk = new int[n], sv = new int[n];
        for (int r = 0; r < n; r++) {
            int i = (int) (keys[r] & 1048575);
            rk[i] = r + 1;
            sv[r] = nums[i];
        }
        int[] cnt = new int[n + 1];
        long[] sm = new long[n + 1];
        int top = Integer.highestOneBit(n);
        long tot = 0;
        for (int i = 0; i < x; i++) {
            for (int p = rk[i]; p <= n; p += p & -p) { cnt[p]++; sm[p] += nums[i]; }
            tot += nums[i];
        }
        int h = (x + 1) / 2;
        long[] cost = new long[m];
        for (int i = 0; i < m; i++) {
            int pos = 0, rem = h;
            long acc = 0;
            for (int pw = top; pw > 0; pw >>= 1) {
                int q = pos + pw;
                if (q <= n && cnt[q] < rem) { pos = q; rem -= cnt[q]; acc += sm[q]; }
            }
            long med = sv[pos], left = acc + med;
            cost[i] = med * h - left + (tot - left) - med * (x - h);
            if (i + 1 < m) {
                int u = nums[i], v = nums[i + x];
                for (int p = rk[i]; p <= n; p += p & -p) { cnt[p]--; sm[p] -= u; }
                for (int p = rk[i + x]; p <= n; p += p & -p) { cnt[p]++; sm[p] += v; }
                tot += v - u;
            }
        }
        long INF = Long.MAX_VALUE / 4;
        long[] prev = new long[n + 1], cur = new long[n + 1];
        for (int j = 1; j <= k; j++) {
            Arrays.fill(cur, INF);
            long best = INF;
            for (int i = j * x; i <= n; i++) {
                long c = prev[i - x] + cost[i - x];
                if (c < best) best = c;
                cur[i] = best;
            }
            long[] t = prev; prev = cur; cur = t;
        }
        return prev[n];
    }
}
