var minimumChanges = function(s, k) {
    const n = s.length, INF = 1e9;
    const b = new Uint8Array(n);
    for (let i = 0; i < n; i++) b[i] = s.charCodeAt(i);
    const w = [];
    for (let e = 0; e < n; e++) w.push(new Int32Array(n).fill(INF));
    for (let d = 1; d <= n >> 1; d++) {
        let pm2 = new Int32Array(n + 1), pm1 = new Int32Array(n + 1);
        for (let L = 2 * d; L <= n; L += d) {
            const cur = new Int32Array(n - L + 1);
            for (let i = 0; i + L <= n; i++) {
                let c = pm2[i + d];
                for (let r = 0; r < d; r++) if (b[i + r] !== b[i + L - d + r]) c++;
                cur[i] = c;
                if (c < w[i + L - 1][i]) w[i + L - 1][i] = c;
            }
            pm2 = pm1;
            pm1 = cur;
        }
    }
    let f = new Int32Array(n + 1).fill(INF);
    for (let i = 2; i <= n - 2 * (k - 1); i++) f[i] = w[i - 1][0];
    for (let j = 2; j <= k; j++) {
        const g = new Int32Array(n + 1).fill(INF);
        const lo = 2 * (j - 1);
        for (let i = 2 * j; i <= n - 2 * (k - j); i++) {
            let best = INF;
            const row = w[i - 1];
            for (let p = lo; p <= i - 2; p++) {
                const v = f[p] + row[p];
                if (v < best) best = v;
            }
            g[i] = best;
        }
        f = g;
    }
    return f[n];
};
