/**
 * @param {number[][]} grid
 * @return {number}
 */
var uniquePaths = function(grid) {
    const M = 1000000007;
    const n = grid[0].length;
    let b = new Int32Array(n), nb = new Int32Array(n);
    b[0] = 1;
    let t = 0;
    for (const row of grid) {
        let a = 0;
        for (let j = 0; j < n; j++) {
            if (row[j] === 1) {
                nb[j] = a;
                a = b[j];
            } else {
                t = (a + b[j]) % M;
                a = nb[j] = t;
            }
        }
        const tmp = b;
        b = nb;
        nb = tmp;
    }
    return t;
};
