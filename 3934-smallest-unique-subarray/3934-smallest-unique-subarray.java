class Solution {
    static final long M = (1L << 61) - 1, B = 100003;

    static long mul(long a, long b) {
        long hi = Math.multiplyHigh(a, b), lo = a * b;
        long r = ((hi << 3) | (lo >>> 61)) + (lo & M);
        return r >= M ? r - M : r;
    }

    public int smallestUniqueSubarray(int[] nums) {
        int n = nums.length;
        long[] H = new long[n + 1];
        for (int i = 0; i < n; i++) {
            long r = mul(H[i], B) + nums[i];
            H[i + 1] = r >= M ? r - M : r;
        }
        long[] v = new long[n];
        int lo = 1, hi = n;
        while (lo < hi) {
            int L = (lo + hi) >>> 1;
            long P = 1, b = B;
            for (int e = L; e > 0; e >>= 1, b = mul(b, b)) if ((e & 1) == 1) P = mul(P, b);
            int m = n - L + 1;
            for (int i = 0; i < m; i++) {
                long s = mul(H[i], P);
                v[i] = H[i + L] >= s ? H[i + L] - s : H[i + L] + M - s;
            }
            java.util.Arrays.sort(v, 0, m);
            boolean ok = false;
            for (int i = 0, j; i < m && !ok; i = j) {
                for (j = i + 1; j < m && v[j] == v[i]; j++);
                if (j - i == 1) ok = true;
            }
            if (ok) hi = L; else lo = L + 1;
        }
        return lo;
    }
}
