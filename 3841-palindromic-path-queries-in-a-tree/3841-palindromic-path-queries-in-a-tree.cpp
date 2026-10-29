class Solution {
public:
    vector<bool> palindromePath(int n, vector<vector<int>>& edges, string s, vector<string>& queries) {
        vector<vector<int>> adj(n);
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        vector<int> val(n), par(n, -1), dep(n, 0), sz(n, 1), heavy(n, -1), best(n, 0), head(n, 0), tin(n, 0), bit(n + 2, 0), order;
        for (int i = 0; i < n; i++) val[i] = 1 << (s[i] - 'a');
        vector<int> pre = val;
        order.reserve(n);
        order.push_back(0);
        for (int k = 0; k < (int)order.size(); k++) {
            int v = order[k], p = par[v];
            for (int w : adj[v]) {
                if (w != p) {
                    par[w] = v;
                    dep[w] = dep[v] + 1;
                    pre[w] ^= pre[v];
                    order.push_back(w);
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
        vector<int> st{0};
        int cnt = 0;
        while (!st.empty()) {
            int v = st.back();
            st.pop_back();
            tin[v] = cnt++;
            int h = heavy[v], p = par[v];
            for (int w : adj[v]) {
                if (w != p && w != h) {
                    head[w] = w;
                    st.push_back(w);
                }
            }
            if (h >= 0) {
                head[h] = head[v];
                st.push_back(h);
            }
        }
        vector<bool> res;
        for (auto& q : queries) {
            int i = q[0] == 'u' ? 7 : 6, u = 0;
            while (q[i] != ' ') u = u * 10 + q[i++] - '0';
            i++;
            if (q[0] == 'u') {
                int d = val[u] ^ (1 << (q[i] - 'a'));
                if (d) {
                    val[u] ^= d;
                    for (int j = tin[u] + 1; j <= n; j += j & -j) bit[j] ^= d;
                    for (int j = tin[u] + sz[u] + 1; j <= n; j += j & -j) bit[j] ^= d;
                }
            } else {
                int v = 0;
                while (i < (int)q.size()) v = v * 10 + q[i++] - '0';
                int x = u, y = v;
                while (head[x] != head[y]) {
                    if (dep[head[x]] > dep[head[y]]) x = par[head[x]];
                    else y = par[head[y]];
                }
                int l = dep[x] < dep[y] ? x : y;
                int m = pre[u] ^ pre[v] ^ val[l];
                for (int j = tin[u] + 1; j; j &= j - 1) m ^= bit[j];
                for (int j = tin[v] + 1; j; j &= j - 1) m ^= bit[j];
                res.push_back((m & (m - 1)) == 0);
            }
        }
        return res;
    }
};
