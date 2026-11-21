class Solution {
public:
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        int n = parent.size();
        vector<int> head(n, -1), nxt(n), np(parent), saved(n), order;
        order.reserve(n);
        for (int i = n - 1; i > 0; --i) { nxt[i] = head[parent[i]]; head[parent[i]] = i; }
        int last[26];
        fill(last, last + 26, -1);
        vector<int> st;
        st.reserve(2 * n + 1);
        st.push_back(0);
        while (!st.empty()) {
            int u = st.back(); st.pop_back();
            if (u >= 0) {
                int c = s[u] - 'a';
                if (last[c] >= 0) np[u] = last[c];
                saved[u] = last[c]; last[c] = u;
                order.push_back(u);
                st.push_back(~u);
                for (int v = head[u]; v != -1; v = nxt[v]) st.push_back(v);
            } else {
                int x = ~u; last[s[x] - 'a'] = saved[x];
            }
        }
        vector<int> sz(n, 1);
        for (int i = n - 1; i > 0; --i) { int u = order[i]; sz[np[u]] += sz[u]; }
        return sz;
    }
};