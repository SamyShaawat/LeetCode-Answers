class Solution {
    public List<Integer> busiestServers(int k, int[] arrival, int[] load) {
        int n = arrival.length;
        int[] free = new int[k];
        for (int i = 0; i < k; i++) free[i] = i;
        int fs = k;
        long[] busy = new long[k];
        int bs = 0;
        int[] cnt = new int[k];
        for (int i = 0; i < n; i++) {
            long a = arrival[i];
            while (bs > 0 && (busy[0] >> 17) <= a) {
                int s = (int) (busy[0] & 131071);
                long last = busy[--bs];
                int p = 0;
                while (true) {
                    int c = 2 * p + 1;
                    if (c >= bs) break;
                    if (c + 1 < bs && busy[c + 1] < busy[c]) c++;
                    if (busy[c] >= last) break;
                    busy[p] = busy[c];
                    p = c;
                }
                if (bs > 0) busy[p] = last;
                int v = i + ((s - i) % k + k) % k;
                int q = fs++;
                while (q > 0) {
                    int par = (q - 1) >> 1;
                    if (free[par] <= v) break;
                    free[q] = free[par];
                    q = par;
                }
                free[q] = v;
            }
            if (fs == 0) continue;
            // lift stale values to >= i
            while (free[0] < i) {
                int v = free[0];
                v += ((i - v + k - 1) / k) * k;
                int p = 0;
                while (true) {
                    int c = 2 * p + 1;
                    if (c >= fs) break;
                    if (c + 1 < fs && free[c + 1] < free[c]) c++;
                    if (free[c] >= v) break;
                    free[p] = free[c];
                    p = c;
                }
                free[p] = v;
            }
            int s = free[0] % k;
            int last = free[--fs];
            int p = 0;
            while (true) {
                int c = 2 * p + 1;
                if (c >= fs) break;
                if (c + 1 < fs && free[c + 1] < free[c]) c++;
                if (free[c] >= last) break;
                free[p] = free[c];
                p = c;
            }
            if (fs > 0) free[p] = last;
            cnt[s]++;
            long e = ((a + load[i]) << 17) | s;
            int q = bs++;
            while (q > 0) {
                int par = (q - 1) >> 1;
                if (busy[par] <= e) break;
                busy[q] = busy[par];
                q = par;
            }
            busy[q] = e;
        }
        int m = 0;
        for (int c : cnt) if (c > m) m = c;
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < k; i++) if (cnt[i] == m) res.add(i);
        return res;
    }
}
