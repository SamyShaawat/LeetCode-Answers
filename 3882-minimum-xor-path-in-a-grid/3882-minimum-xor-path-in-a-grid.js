/**
 * @param {number[][]} grid
 * @return {number}
 */
var minCost = function(grid) {
    const M = [0x55555555, 0x33333333, 0x0F0F0F0F, 0x00FF00FF, 0x0000FFFF];
    const m = grid.length, n = grid[0].length;
    const cur = new Int32Array(n * 32), s = new Int32Array(32);
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const g = grid[i][j];
            if (i === 0 && j === 0) {
                cur[g >> 5] = 1 << (g & 31);
                continue;
            }
            if (i === 0) for (let k = 0; k < 32; k++) s[k] = cur[(j - 1) * 32 + k];
            else if (j === 0) for (let k = 0; k < 32; k++) s[k] = cur[k];
            else for (let k = 0; k < 32; k++) s[k] = cur[j * 32 + k] | cur[(j - 1) * 32 + k];
            for (let b = 0; b < 5; b++) {
                if ((g >> b) & 1) {
                    const w = 1 << b, mk = M[b];
                    for (let k = 0; k < 32; k++) s[k] = ((s[k] & mk) << w) | ((s[k] >>> w) & mk);
                }
            }
            for (let b = 5; b < 10; b++) {
                if ((g >> b) & 1) {
                    const d = 1 << (b - 5);
                    for (let k = 0; k < 32; k++) {
                        if ((k & d) === 0) {
                            const t = s[k];
                            s[k] = s[k | d];
                            s[k | d] = t;
                        }
                    }
                }
            }
            for (let k = 0; k < 32; k++) cur[j * 32 + k] = s[k];
        }
    }
    const base = (n - 1) * 32;
    for (let k = 0; k < 32; k++) {
        const v = cur[base + k];
        if (v !== 0) return k * 32 + (31 - Math.clz32(v & -v));
    }
    return 0;
};
