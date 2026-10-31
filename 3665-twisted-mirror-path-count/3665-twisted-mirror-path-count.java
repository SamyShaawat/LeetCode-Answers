class Solution {
    public int uniquePaths(int[][] grid) {
        final int M = 1000000007;
        int n = grid[0].length;
        int[] b = new int[n], nb = new int[n];
        b[0] = 1;
        int t = 0;
        for (int[] row : grid) {
            int a = 0;
            for (int j = 0; j < n; j++) {
                if (row[j] == 1) {
                    nb[j] = a;
                    a = b[j];
                } else {
                    t = (a + b[j]) % M;
                    a = nb[j] = t;
                }
            }
            int[] tmp = b;
            b = nb;
            nb = tmp;
        }
        return t;
    }
}
