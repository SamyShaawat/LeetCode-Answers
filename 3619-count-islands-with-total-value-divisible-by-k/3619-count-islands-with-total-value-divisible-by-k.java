class Solution {
    public int countIslands(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length, ans = 0;
        int[] st = new int[m * n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) continue;
                long s = grid[i][j];
                grid[i][j] = 0;
                int top = 0;
                st[top++] = i * n + j;
                while (top > 0) {
                    int p = st[--top];
                    int r = p / n, c = p % n;
                    if (r > 0 && grid[r - 1][c] != 0) { s += grid[r - 1][c]; grid[r - 1][c] = 0; st[top++] = p - n; }
                    if (r + 1 < m && grid[r + 1][c] != 0) { s += grid[r + 1][c]; grid[r + 1][c] = 0; st[top++] = p + n; }
                    if (c > 0 && grid[r][c - 1] != 0) { s += grid[r][c - 1]; grid[r][c - 1] = 0; st[top++] = p - 1; }
                    if (c + 1 < n && grid[r][c + 1] != 0) { s += grid[r][c + 1]; grid[r][c + 1] = 0; st[top++] = p + 1; }
                }
                if (s % k == 0) ans++;
            }
        }
        return ans;
    }
}
