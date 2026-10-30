/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {string} labels
 * @param {number} k
 * @return {number}
 */
var shortestPath = function (n, edges, labels, k) {
    const K = k + 1, m = edges.length, B = 4194304;
    const head = new Int32Array(n + 1), to = new Int32Array(m), wt = new Int32Array(m);
    for (let i = 0; i < m; i++) head[edges[i][0] + 1]++;
    for (let i = 0; i < n; i++) head[i + 1] += head[i];
    const pos = head.slice(0, n);
    for (let i = 0; i < m; i++) {
        const e = edges[i], p = pos[e[0]]++;
        to[p] = e[1];
        wt[p] = e[2];
    }
    const lab = new Uint8Array(n);
    for (let i = 0; i < n; i++) lab[i] = labels.charCodeAt(i);
    const dist = new Int32Array(n * K).fill(2147483647);
    const minc = new Int32Array(n).fill(K);
    dist[1] = 0;
    const h = new Float64Array(m * K + 2);
    let sz = 1;
    h[0] = 1;
    while (sz > 0) {
        const x = h[0];
        const last = h[--sz];
        if (sz > 0) {
            let i = 0;
            for (;;) {
                let c = 2 * i + 1;
                if (c >= sz) break;
                if (c + 1 < sz && h[c + 1] < h[c]) c++;
                if (h[c] >= last) break;
                h[i] = h[c];
                i = c;
            }
            h[i] = last;
        }
        const d = Math.floor(x / B), s = x - d * B;
        if (d > dist[s]) continue;
        const u = (s / K) | 0, c = s - u * K;
        if (c >= minc[u]) continue;
        if (u === n - 1) return d;
        minc[u] = c;
        for (let i = head[u], end = head[u + 1]; i < end; i++) {
            const v = to[i];
            let nc;
            if (lab[v] === lab[u]) {
                nc = c + 1;
                if (nc >= minc[v]) continue;
            } else {
                if (minc[v] === 1) continue;
                nc = 1;
            }
            const t = v * K + nc, nd = d + wt[i];
            if (nd < dist[t]) {
                dist[t] = nd;
                const val = nd * B + t;
                let j = sz++;
                while (j > 0) {
                    const p = (j - 1) >> 1;
                    if (h[p] <= val) break;
                    h[j] = h[p];
                    j = p;
                }
                h[j] = val;
            }
        }
    }
    return -1;
};
