/**
 * @param {number[]} nums
 * @param {number} x
 * @param {number} k
 * @return {number}
 */
var minOperations = function (nums, x, k) {
    const n = nums.length, m = n - x + 1;
    const id = new Int32Array(n);
    for (let i = 0; i < n; i++) id[i] = i;
    id.sort((a, b) => nums[a] - nums[b] || a - b);
    const rk = new Int32Array(n), sv = new Int32Array(n);
    for (let r = 0; r < n; r++) { rk[id[r]] = r + 1; sv[r] = nums[id[r]]; }
    const cnt = new Int32Array(n + 1), sm = new Float64Array(n + 1);
    let top = 1;
    while (top * 2 <= n) top *= 2;
    let tot = 0;
    for (let i = 0; i < x; i++) {
        for (let p = rk[i]; p <= n; p += p & -p) { cnt[p]++; sm[p] += nums[i]; }
        tot += nums[i];
    }
    const h = (x + 1) >> 1;
    const cost = new Float64Array(m);
    for (let i = 0; i < m; i++) {
        let pos = 0, rem = h, acc = 0;
        for (let pw = top; pw > 0; pw >>= 1) {
            const q = pos + pw;
            if (q <= n && cnt[q] < rem) { pos = q; rem -= cnt[q]; acc += sm[q]; }
        }
        const med = sv[pos], left = acc + med;
        cost[i] = med * h - left + (tot - left) - med * (x - h);
        if (i + 1 < m) {
            const u = nums[i], v = nums[i + x];
            for (let p = rk[i]; p <= n; p += p & -p) { cnt[p]--; sm[p] -= u; }
            for (let p = rk[i + x]; p <= n; p += p & -p) { cnt[p]++; sm[p] += v; }
            tot += v - u;
        }
    }
    const INF = 1e18;
    let prev = new Float64Array(n + 1), cur = new Float64Array(n + 1);
    for (let j = 1; j <= k; j++) {
        cur.fill(INF);
        let best = INF;
        for (let i = j * x; i <= n; i++) {
            const c = prev[i - x] + cost[i - x];
            if (c < best) best = c;
            cur[i] = best;
        }
        const t = prev; prev = cur; cur = t;
    }
    return prev[n];
};
