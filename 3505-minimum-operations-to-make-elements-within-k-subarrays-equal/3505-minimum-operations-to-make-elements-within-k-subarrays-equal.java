class Solution {
    public long minOperations(int[] nums, int x, int k) {
        int n = nums.length;
        final int O = 1000000, SH = 17;
        final long M = (1L << SH) - 1;
        PriorityQueue<Long> lo = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Long> hi = new PriorityQueue<>();
        boolean[] side = new boolean[n];
        long ls = 0, hs = 0;
        int lc = 0, hc = 0;
        long[] c = new long[n];
        for (int i = 0; i < n; i++) {
            int v = nums[i];
            long key = ((long) (v + O) << SH) | i;
            if (!lo.isEmpty() && key < lo.peek()) { lo.add(key); ls += v; lc++; side[i] = true; }
            else { hi.add(key); hs += v; hc++; }
            long lim = i - x;
            if (i >= x) {
                int u = nums[(int) lim];
                if (side[(int) lim]) { lc--; ls -= u; }
                else { hc--; hs -= u; }
                while (!lo.isEmpty() && (lo.peek() & M) <= lim) lo.poll();
                while (!hi.isEmpty() && (hi.peek() & M) <= lim) hi.poll();
            }
            while (lc > hc + 1) {
                long t = lo.poll(); lc--;
                long tv = (t >> SH) - O;
                ls -= tv; hi.add(t); hc++; hs += tv; side[(int) (t & M)] = false;
                while (!lo.isEmpty() && (lo.peek() & M) <= lim) lo.poll();
            }
            while (lc < hc) {
                long t = hi.poll(); hc--;
                long tv = (t >> SH) - O;
                hs -= tv; lo.add(t); lc++; ls += tv; side[(int) (t & M)] = true;
                while (!hi.isEmpty() && (hi.peek() & M) <= lim) hi.poll();
            }
            if (i >= x - 1) {
                long m = (lo.peek() >> SH) - O;
                c[i - x + 1] = m * lc - ls + hs - m * hc;
            }
        }
        final long INF = Long.MAX_VALUE / 2;
        long[] prev = new long[n + 1];
        long[] cur = new long[n + 1];
        for (int j = 1; j <= k; j++) {
            Arrays.fill(cur, INF);
            for (int i = j * x; i <= n; i++) {
                long a = prev[i - x] + c[i - x];
                long b = cur[i - 1];
                cur[i] = a < b ? a : b;
            }
            long[] t = prev; prev = cur; cur = t;
        }
        return prev[n];
    }
}
