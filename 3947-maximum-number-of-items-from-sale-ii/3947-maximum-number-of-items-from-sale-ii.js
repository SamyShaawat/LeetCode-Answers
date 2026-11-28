/**
 * @param {number[][]} items
 * @param {number} budget
 * @return {number}
 */
var maximumSaleItems = function(items, budget) {
    const n = items.length;
    const cnt = new Int32Array(n + 1);
    const D = new Int32Array(n + 1);
    let m = Infinity;
    for (const [f, p] of items) {
        cnt[f]++;
        if (p < m) m = p;
    }
    for (let v = 1; v <= n; v++) {
        if (!cnt[v]) continue;
        let s = 0;
        for (let w = v; w <= n; w += v) s += cnt[w];
        D[v] = s - 1;
    }
    const lim = 2 * m;
    const keys = new Float64Array(n);
    let g = 0;
    for (const [f, p] of items)
        if (p <= lim && D[f] > 0) keys[g++] = p * 131072 + D[f];
    const sorted = keys.subarray(0, g).sort();
    let t = 0, R = budget;
    for (let i = 0; i < g; i++) {
        const c = Math.floor(sorted[i] / 131072);
        const k = sorted[i] % 131072;
        const x = Math.floor(R / c);
        if (x < k) {
            t += x;
            R -= x * c;
            break;
        }
        t += k;
        R -= k * c;
    }
    return 2 * t + Math.floor(R / m);
};
