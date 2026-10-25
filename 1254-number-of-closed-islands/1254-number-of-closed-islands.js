/**
 * @param {number[][]} grid
 * @return {number}
 */
var closedIsland = function(grid) {
    const m = grid.length, n = grid[0].length;
    let res = 0;
    const st = new Int32Array(m * n);
    for (let i = 1; i < m - 1; i++) {
        for (let j = 1; j < n - 1; j++) {
            if (grid[i][j] !== 0) continue;
            grid[i][j] = 1;
            let top = 0;
            st[top++] = i * n + j;
            let ok = 1;
            while (top > 0) {
                const p = st[--top];
                const x = (p / n) | 0, y = p - x * n;
                if (x === 0 || y === 0 || x === m - 1 || y === n - 1) {
                    ok = 0;
                    continue;
                }
                if (grid[x + 1][y] === 0) { grid[x + 1][y] = 1; st[top++] = p + n; }
                if (grid[x - 1][y] === 0) { grid[x - 1][y] = 1; st[top++] = p - n; }
                if (grid[x][y + 1] === 0) { grid[x][y + 1] = 1; st[top++] = p + 1; }
                if (grid[x][y - 1] === 0) { grid[x][y - 1] = 1; st[top++] = p - 1; }
            }
            res += ok;
        }
    }
    return res;
};
