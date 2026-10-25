class Solution {
    public int closedIsland(int[][] grid) {
        int m = grid.length, n = grid[0].length, res = 0;
        int[] st = new int[m * n];
        for (int i = 1; i < m - 1; i++) {
            for (int j = 1; j < n - 1; j++) {
                if (grid[i][j] != 0) continue;
                grid[i][j] = 1;
                int top = 0;
                st[top++] = i * n + j;
                int ok = 1;
                while (top > 0) {
                    int p = st[--top];
                    int x = p / n, y = p % n;
                    if (x == 0 || y == 0 || x == m - 1 || y == n - 1) {
                        ok = 0;
                        continue;
                    }
                    if (grid[x + 1][y] == 0) { grid[x + 1][y] = 1; st[top++] = p + n; }
                    if (grid[x - 1][y] == 0) { grid[x - 1][y] = 1; st[top++] = p - n; }
                    if (grid[x][y + 1] == 0) { grid[x][y + 1] = 1; st[top++] = p + 1; }
                    if (grid[x][y - 1] == 0) { grid[x][y - 1] = 1; st[top++] = p - 1; }
                }
                res += ok;
            }
        }
        return res;
    }
}
