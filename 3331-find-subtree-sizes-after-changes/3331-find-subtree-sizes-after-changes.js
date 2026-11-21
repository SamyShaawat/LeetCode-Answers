var findSubtreeSizes = function(parent, s) {
    const n = parent.length;
    const head = new Int32Array(n).fill(-1), nxt = new Int32Array(n);
    for (let i = n - 1; i > 0; i--) { nxt[i] = head[parent[i]]; head[parent[i]] = i; }
    const c = new Int32Array(n);
    for (let i = 0; i < n; i++) c[i] = s.charCodeAt(i) - 97;
    const last = new Int32Array(26).fill(-1), saved = new Int32Array(n);
    const np = Int32Array.from(parent), order = new Int32Array(n);
    const st = new Int32Array(2 * n + 1);
    let top = 0, k = 0;
    st[top++] = 0;
    while (top) {
        const u = st[--top];
        if (u >= 0) {
            const ch = c[u];
            if (last[ch] >= 0) np[u] = last[ch];
            saved[u] = last[ch]; last[ch] = u; order[k++] = u;
            st[top++] = ~u;
            for (let v = head[u]; v !== -1; v = nxt[v]) st[top++] = v;
        } else {
            const x = ~u; last[c[x]] = saved[x];
        }
    }
    const sz = new Array(n).fill(1);
    for (let i = n - 1; i > 0; i--) { const u = order[i]; sz[np[u]] += sz[u]; }
    return sz;
};