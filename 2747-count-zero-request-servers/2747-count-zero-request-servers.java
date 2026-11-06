class Solution {
    public int[] countServers(int n, int[][] logs, int x, int[] queries) {
        Arrays.sort(logs, (a, b) -> a[1] - b[1]);
        int k = queries.length;
        long[] keys = new long[k];
        for (int i = 0; i < k; i++) keys[i] = ((long) queries[i] << 20) | i;
        Arrays.sort(keys);
        int[] cnt = new int[n + 1];
        int[] res = new int[k];
        int m = logs.length, lo = 0, hi = 0, active = 0;
        for (long key : keys) {
            int qi = (int) (key & 0xFFFFF), q = (int) (key >> 20), left = q - x;
            while (hi < m && logs[hi][1] <= q) {
                if (cnt[logs[hi][0]]++ == 0) active++;
                hi++;
            }
            while (lo < hi && logs[lo][1] < left) {
                if (--cnt[logs[lo][0]] == 0) active--;
                lo++;
            }
            res[qi] = n - active;
        }
        return res;
    }
}
