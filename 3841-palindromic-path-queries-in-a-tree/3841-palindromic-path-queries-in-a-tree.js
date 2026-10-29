/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {string} s
 * @param {string[]} queries
 * @return {boolean[]}
 */
var palindromePath = function(n, edges, s, queries) {
    const head = new Int32Array(n).fill(-1), nxt = new Int32Array(2 * n), to = new Int32Array(2 * n);
    let ec = 0;
    for (const e of edges) {
        to[ec] = e[1]; nxt[ec] = head[e[0]]; head[e[0]] = ec++;
        to[ec] = e[0]; nxt[ec] = head[e[1]]; head[e[1]] = ec++;
    }
    const cur = new Int32Array(n), par = new Int32Array(n), pre = new Int32Array(n), dep = new Int32Array(n);
    const tin = new Int32Array(n), order = new Int32Array(n), sz = new Int32Array(n).fill(1);
    for (let i = 0; i < n; i++) cur[i] = 1 << (s.charCodeAt(i) - 97);
    par[0] = -1;
    pre[0] = cur[0];
    const st = new Int32Array(n);
    let top = 0, cnt = 0;
    st[top++] = 0;
    while (top > 0) {
        const u = st[--top];
        tin[u] = cnt;
        order[cnt++] = u;
        for (let e = head[u]; e >= 0; e = nxt[e]) {
            const w = to[e];
            if (w !== par[u]) {
                par[w] = u;
                dep[w] = dep[u] + 1;
                pre[w] = pre[u] ^ cur[w];
                st[top++] = w;
            }
        }
    }
    for (let i = n - 1; i > 0; i--) sz[par[order[i]]] += sz[order[i]];
    // key = dep * 65536 + par, kept in a double (no 32-bit overflow)
    const sp = [new Float64Array(n)];
    for (let i = 0; i < n; i++) sp[0][i] = dep[order[i]] * 65536 + par[order[i]];
    for (let k = 1; (1 << k) <= n; k++) {
        const prev = sp[k - 1], row = new Float64Array(n - (1 << k) + 1), h = 1 << (k - 1);
        for (let i = 0; i < row.length; i++) row[i] = prev[i] < prev[i + h] ? prev[i] : prev[i + h];
        sp.push(row);
    }
    const bit = new Int32Array(n + 2);
    const ans = [];
    for (const q of queries) {
        let u = 0, p = q.indexOf(' ') + 1;
        while (q.charCodeAt(p) !== 32) u = u * 10 + q.charCodeAt(p++) - 48;
        p++;
        if (q.charCodeAt(0) === 117) {
            const c = 1 << (q.charCodeAt(p) - 97);
            const d = cur[u] ^ c;
            if (d !== 0) {
                cur[u] = c;
                for (let i = tin[u] + 1; i <= n; i += i & -i) bit[i] ^= d;
                for (let i = tin[u] + sz[u] + 1; i <= n; i += i & -i) bit[i] ^= d;
            }
        } else {
            let v = 0;
            const len = q.length;
            while (p < len) v = v * 10 + q.charCodeAt(p++) - 48;
            let x = pre[u] ^ pre[v];
            for (let i = tin[u] + 1; i !== 0; i &= i - 1) x ^= bit[i];
            for (let i = tin[v] + 1; i !== 0; i &= i - 1) x ^= bit[i];
            let lo = tin[u], hi = tin[v], l;
            if (lo > hi) { const t = lo; lo = hi; hi = t; }
            if (lo === hi) l = u;
            else {
                lo++;
                const k = 31 - Math.clz32(hi - lo + 1);
                const a = sp[k][lo], b = sp[k][hi - (1 << k) + 1];
                l = (a < b ? a : b) % 65536;
            }
            x ^= cur[l];
            ans.push((x & (x - 1)) === 0);
        }
    }
    return ans;
};
