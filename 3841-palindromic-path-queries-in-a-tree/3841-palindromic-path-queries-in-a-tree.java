class Solution {
    public List<Boolean> palindromePath(int n, int[][] edges, String s, String[] queries) {
        int[] deg = new int[n + 1];
        for (int[] e : edges) {
            deg[e[0] + 1]++;
            deg[e[1] + 1]++;
        }
        for (int i = 0; i < n; i++) deg[i + 1] += deg[i];
        int[] pos = deg.clone(), adj = new int[2 * (n - 1)];
        for (int[] e : edges) {
            adj[pos[e[0]]++] = e[1];
            adj[pos[e[1]]++] = e[0];
        }
        int[] val = new int[n], par = new int[n], dep = new int[n], pre = new int[n], order = new int[n];
        int[] sz = new int[n], heavy = new int[n], best = new int[n], head = new int[n], tin = new int[n], bit = new int[n + 2];
        for (int i = 0; i < n; i++) {
            val[i] = 1 << (s.charAt(i) - 'a');
            sz[i] = 1;
            heavy[i] = -1;
        }
        par[0] = -1;
        pre[0] = val[0];
        int tail = 1;
        for (int k = 0; k < tail; k++) {
            int v = order[k], p = par[v];
            for (int j = deg[v]; j < deg[v + 1]; j++) {
                int w = adj[j];
                if (w != p) {
                    par[w] = v;
                    dep[w] = dep[v] + 1;
                    pre[w] = pre[v] ^ val[w];
                    order[tail++] = w;
                }
            }
        }
        for (int k = n - 1; k > 0; k--) {
            int v = order[k], p = par[v];
            sz[p] += sz[v];
            if (sz[v] > best[p]) {
                best[p] = sz[v];
                heavy[p] = v;
            }
        }
        int[] st = new int[n];
        int top = 0, cnt = 0;
        st[top++] = 0;
        while (top > 0) {
            int v = st[--top];
            tin[v] = cnt++;
            int h = heavy[v], p = par[v];
            for (int j = deg[v]; j < deg[v + 1]; j++) {
                int w = adj[j];
                if (w != p && w != h) {
                    head[w] = w;
                    st[top++] = w;
                }
            }
            if (h >= 0) {
                head[h] = head[v];
                st[top++] = h;
            }
        }
        List<Boolean> res = new ArrayList<>();
        for (String q : queries) {
            String[] parts = q.split(" ");
            int u = Integer.parseInt(parts[1]);
            if (parts[0].charAt(0) == 'u') {
                int d = val[u] ^ (1 << (parts[2].charAt(0) - 'a'));
                if (d != 0) {
                    val[u] ^= d;
                    for (int j = tin[u] + 1; j <= n; j += j & -j) bit[j] ^= d;
                    for (int j = tin[u] + sz[u] + 1; j <= n; j += j & -j) bit[j] ^= d;
                }
            } else {
                int v = Integer.parseInt(parts[2]);
                int x = u, y = v;
                while (head[x] != head[y]) {
                    if (dep[head[x]] > dep[head[y]]) x = par[head[x]];
                    else y = par[head[y]];
                }
                int l = dep[x] < dep[y] ? x : y;
                int m = pre[u] ^ pre[v] ^ val[l];
                for (int j = tin[u] + 1; j > 0; j &= j - 1) m ^= bit[j];
                for (int j = tin[v] + 1; j > 0; j &= j - 1) m ^= bit[j];
                res.add((m & (m - 1)) == 0);
            }
        }
        return res;
    }
}
