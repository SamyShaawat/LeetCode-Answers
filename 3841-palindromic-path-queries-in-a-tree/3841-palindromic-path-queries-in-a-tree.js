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
    for (const [x, y] of edges) {
        to[ec] = y; nxt[ec] = head[x]; head[x] = ec++;
        to[ec] = x; nxt[ec] = head[y]; head[y] = ec++;
    }
    const a = new Int32Array(n), tin = new Int32Array(n), tout = new Int32Array(n);
    const base = new Int32Array(n), order = new Int32Array(n), up = new Int32Array(n).fill(-1);
    for (let i = 0; i < n; i++) a[i] = 1 << (s.charCodeAt(i) - 97);
    base[0] = a[0];
    const stack = new Int32Array(2 * n);
    let sp = 0, t = 0;
    stack[sp++] = 0;
    while (sp > 0) {
        const u = stack[--sp];
        if (u >= 0) {
            tin[u] = ++t;
            order[t - 1] = u;
            stack[sp++] = ~u;
            for (let e = head[u]; e >= 0; e = nxt[e]) {
                const v = to[e];
                if (v !== up[u]) {
                    up[v] = u;
                    base[v] = base[u] ^ a[v];
                    stack[sp++] = v;
                }
            }
        } else {
            tout[~u] = t;
        }
    }
    const LOG = 32 - Math.clz32(n);
    const table = [];
    for (let j = 0; j < LOG; j++) table.push(new Int32Array(n));
    for (let i = 1; i < n; i++) table[0][i] = tin[up[order[i]]];
    for (let j = 1; (1 << j) <= n; j++)
        for (let i = 0; i + (1 << j) <= n; i++)
            table[j][i] = Math.min(table[j - 1][i], table[j - 1][i + (1 << (j - 1))]);
    const bit = new Int32Array(n + 2), size = n + 1;
    const ans = [];
    for (const q of queries) {
        if (q.charCodeAt(0) === 117) {
            const p = q.indexOf(' ', 7);
            const u = parseInt(q.substring(7, p));
            const m = a[u] ^ (1 << (q.charCodeAt(p + 1) - 97));
            if (m !== 0) {
                a[u] ^= m;
                for (let i = tin[u]; i <= size; i += i & -i) bit[i] ^= m;
                for (let i = tout[u] + 1; i <= size; i += i & -i) bit[i] ^= m;
            }
        } else {
            const p = q.indexOf(' ', 6);
            const u = parseInt(q.substring(6, p)), v = parseInt(q.substring(p + 1));
            let l = tin[u], r = tin[v];
            if (l > r) { const x = l; l = r; r = x; }
            let w;
            if (l === r) w = u;
            else {
                const k = 31 - Math.clz32(r - l);
                w = order[Math.min(table[k][l], table[k][r - (1 << k)]) - 1];
            }
            let m = base[u] ^ base[v] ^ a[w];
            for (let i = tin[u]; i; i &= i - 1) m ^= bit[i];
            for (let i = tin[v]; i; i &= i - 1) m ^= bit[i];
            ans.push((m & (m - 1)) === 0);
        }
    }
    return ans;
};
