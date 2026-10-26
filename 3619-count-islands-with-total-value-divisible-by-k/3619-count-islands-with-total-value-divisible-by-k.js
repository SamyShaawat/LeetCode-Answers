/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number}
 */
var countIslands = function(grid, k) {
    const m = grid.length, n = grid[0].length;
    const st = new Int32Array(m * n);
    let ans = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 0) continue;
            let s = grid[i][j];
            grid[i][j] = 0;
            let top = 0;
            st[top++] = i * n + j;
            while (top > 0) {
                const p = st[--top];
                const r = (p / n) | 0, c = p - r * n;
                if (r > 0 && grid[r - 1][c] !== 0) { s += grid[r - 1][c]; grid[r - 1][c] = 0; st[top++] = p - n; }
                if (r + 1 < m && grid[r + 1][c] !== 0) { s += grid[r + 1][c]; grid[r + 1][c] = 0; st[top++] = p + n; }
                if (c > 0 && grid[r][c - 1] !== 0) { s += grid[r][c - 1]; grid[r][c - 1] = 0; st[top++] = p - 1; }
                if (c + 1 < n && grid[r][c + 1] !== 0) { s += grid[r][c + 1]; grid[r][c + 1] = 0; st[top++] = p + 1; }
            }
            if (s % k === 0) ans++;
        }
    }
    return ans;
};
