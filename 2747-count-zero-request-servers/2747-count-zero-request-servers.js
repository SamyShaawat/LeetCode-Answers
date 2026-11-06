/**
 * @param {number} n
 * @param {number[][]} logs
 * @param {number} x
 * @param {number[]} queries
 * @return {number[]}
 */
var countServers = function(n, logs, x, queries) {
    logs.sort((a, b) => a[1] - b[1]);
    const k = queries.length;
    const order = new Int32Array(k);
    for (let i = 0; i < k; i++) order[i] = i;
    order.sort((a, b) => queries[a] - queries[b]);
    const cnt = new Int32Array(n + 1);
    const res = new Array(k);
    const m = logs.length;
    let lo = 0, hi = 0, active = 0;
    for (let j = 0; j < k; j++) {
        const qi = order[j], q = queries[qi], left = q - x;
        while (hi < m && logs[hi][1] <= q) {
            if (cnt[logs[hi][0]]++ === 0) active++;
            hi++;
        }
        while (lo < hi && logs[lo][1] < left) {
            if (--cnt[logs[lo][0]] === 0) active--;
            lo++;
        }
        res[qi] = n - active;
    }
    return res;
};
