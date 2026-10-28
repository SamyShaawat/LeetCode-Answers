class Solution {
    public int minCost(int[][] grid) {
        final long[] M = {0x5555555555555555L, 0x3333333333333333L, 0x0F0F0F0F0F0F0F0FL,
                0x00FF00FF00FF00FFL, 0x0000FFFF0000FFFFL, 0x00000000FFFFFFFFL};
        int m = grid.length, n = grid[0].length;
        long[][] cur = new long[n][16];
        long[] s = new long[16];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int g = grid[i][j];
                if (i == 0 && j == 0) {
                    cur[0][g >> 6] = 1L << (g & 63);
                    continue;
                }
                if (i == 0) System.arraycopy(cur[j - 1], 0, s, 0, 16);
                else if (j == 0) System.arraycopy(cur[0], 0, s, 0, 16);
                else for (int k = 0; k < 16; k++) s[k] = cur[j][k] | cur[j - 1][k];
                for (int b = 0; b < 6; b++) {
                    if (((g >> b) & 1) != 0) {
                        int w = 1 << b;
                        long mk = M[b];
                        for (int k = 0; k < 16; k++) s[k] = ((s[k] & mk) << w) | ((s[k] >>> w) & mk);
                    }
                }
                for (int b = 6; b < 10; b++) {
                    if (((g >> b) & 1) != 0) {
                        int d = 1 << (b - 6);
                        for (int k = 0; k < 16; k++) {
                            if ((k & d) == 0) {
                                long t = s[k];
                                s[k] = s[k | d];
                                s[k | d] = t;
                            }
                        }
                    }
                }
                System.arraycopy(s, 0, cur[j], 0, 16);
            }
        }
        long[] r = cur[n - 1];
        for (int k = 0; k < 16; k++) if (r[k] != 0) return (k << 6) + Long.numberOfTrailingZeros(r[k]);
        return 0;
    }
}
