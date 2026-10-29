class Solution {
public:
    vector<bool> palindromePath(int n, vector<vector<int>>& edges, string s, vector<string>& queries) {
        vector<vector<int>> adj(n);
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        vector<int> cur(n), par(n, -1), pre(n), dep(n), tin(n), order, sz(n, 1);
        for (int i = 0; i < n; i++) cur[i] = 1 << (s[i] - 'a');
        pre[0] = cur[0];
        order.reserve(n);
        vector<int> st{0};
        while (!st.empty()) {
            int u = st.back();
            st.pop_back();
            tin[u] = order.size();
            order.push_back(u);
            for (int w : adj[u]) {
                if (w != par[u]) {
                    par[w] = u;
                    dep[w] = dep[u] + 1;
                    pre[w] = pre[u] ^ cur[w];
                    st.push_back(w);
                }
            }
        }
        for (int i = n - 1; i > 0; i--) sz[par[order[i]]] += sz[order[i]];
        int LOG = 1;
        while ((1 << LOG) <= n) LOG++;
        vector<vector<long long>> sp(LOG, vector<long long>(n));
        for (int i = 0; i < n; i++) sp[0][i] = ((long long)dep[order[i]] << 16) | par[order[i]];
        for (int k = 1; k < LOG; k++)
            for (int i = 0; i + (1 << k) <= n; i++)
                sp[k][i] = min(sp[k - 1][i], sp[k - 1][i + (1 << (k - 1))]);
        vector<int> bit(n + 2, 0);
        vector<bool> ans;
        for (auto& q : queries) {
            int u = 0, p = q.find(' ') + 1;
            while (q[p] != ' ') u = u * 10 + q[p++] - '0';
            p++;
            if (q[0] == 'u') {
                int c = 1 << (q[p] - 'a');
                int d = cur[u] ^ c;
                if (d) {
                    cur[u] = c;
                    for (int i = tin[u] + 1; i <= n; i += i & -i) bit[i] ^= d;
                    for (int i = tin[u] + sz[u] + 1; i <= n; i += i & -i) bit[i] ^= d;
                }
            } else {
                int v = 0;
                while (p < (int)q.size()) v = v * 10 + q[p++] - '0';
                int x = pre[u] ^ pre[v];
                for (int i = tin[u] + 1; i; i &= i - 1) x ^= bit[i];
                for (int i = tin[v] + 1; i; i &= i - 1) x ^= bit[i];
                int lo = tin[u], hi = tin[v], l;
                if (lo > hi) swap(lo, hi);
                if (lo == hi) l = u;
                else {
                    lo++;
                    int k = 31 - __builtin_clz(hi - lo + 1);
                    l = (int)(min(sp[k][lo], sp[k][hi - (1 << k) + 1]) & 65535);
                }
                x ^= cur[l];
                ans.push_back((x & (x - 1)) == 0);
            }
        }
        return ans;
    }
};
