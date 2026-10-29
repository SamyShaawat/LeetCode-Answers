var palindromePath = function(n, edges, s, queries) {
    const deg = new Int32Array(n + 1);
    for (const e of edges) {
        deg[e[0] + 1]++;
        deg[e[1] + 1]++;
    }
    for (let i = 0; i < n; i++) deg[i + 1] += deg[i];
    const pos = deg.slice(), adj = new Int32Array(2 * (n - 1));
    for (const e of edges) {
        adj[pos[e[0]]++] = e[1];
        adj[pos[e[1]]++] = e[0];
    }
    const val = new Int32Array(n), par = new Int32Array(n), dep = new Int32Array(n), pre = new Int32Array(n), order = new Int32Array(n);
    const sz = new Int32Array(n).fill(1), heavy = new Int32Array(n).fill(-1), best = new Int32Array(n), head = new Int32Array(n), tin = new Int32Array(n), bit = new Int32Array(n + 2);
    for (let i = 0; i < n; i++) val[i] = 1 << (s.charCodeAt(i) - 97);
    par[0] = -1;
    pre[0] = val[0];
    let tail = 1;
    for (let k = 0; k < tail; k++) {
        const v = order[k], p = par[v];
        for (let j = deg[v]; j < deg[v + 1]; j++) {
            const w = adj[j];
            if (w !== p) {
                par[w] = v;
                dep[w] = dep[v] + 1;
                pre[w] = pre[v] ^ val[w];
                order[tail++] = w;
            }
        }
    }
    for (let k = n - 1; k > 0; k--) {
        const v = order[k], p = par[v];
        sz[p] += sz[v];
        if (sz[v] > best[p]) {
            best[p] = sz[v];
            heavy[p] = v;
        }
    }
    const st = new Int32Array(n);
    let top = 0, cnt = 0;
    st[top++] = 0;
    while (top > 0) {
        const v = st[--top];
        tin[v] = cnt++;
        const h = heavy[v], p = par[v];
        for (let j = deg[v]; j < deg[v + 1]; j++) {
            const w = adj[j];
            if (w !== p && w !== h) {
                head[w] = w;
                st[top++] = w;
            }
        }
        if (h >= 0) {
            head[h] = head[v];
            st[top++] = h;
        }
    }
    const res = [];
    for (const q of queries) {
        const parts = q.split(" ");
        const u = +parts[1];
        if (parts[0] === "update") {
            const d = val[u] ^ (1 << (parts[2].charCodeAt(0) - 97));
            if (d) {
                val[u] ^= d;
                for (let j = tin[u] + 1; j <= n; j += j & -j) bit[j] ^= d;
                for (let j = tin[u] + sz[u] + 1; j <= n; j += j & -j) bit[j] ^= d;
            }
        } else {
            const v = +parts[2];
            let x = u, y = v;
            while (head[x] !== head[y]) {
                if (dep[head[x]] > dep[head[y]]) x = par[head[x]];
                else y = par[head[y]];
            }
            const l = dep[x] < dep[y] ? x : y;
            let m = pre[u] ^ pre[v] ^ val[l];
            for (let j = tin[u] + 1; j > 0; j &= j - 1) m ^= bit[j];
            for (let j = tin[v] + 1; j > 0; j &= j - 1) m ^= bit[j];
            res.push((m & (m - 1)) === 0);
        }
    }
    return res;
};
