class Solution {
public:
    vector<bool> palindromePath(int n, vector<vector<int>>& edges, string s, vector<string>& queries) {
        vector<int> head(n, -1), nxt(2 * n), to(2 * n);
        int ec = 0;
        for (auto& e : edges) {
            to[ec] = e[1]; nxt[ec] = head[e[0]]; head[e[0]] = ec++;
            to[ec] = e[0]; nxt[ec] = head[e[1]]; head[e[1]] = ec++;
        }
        vector<int> a(n), tin(n), tout(n), base(n), order(n), up(n, -1);
        for (int i = 0; i < n; i++) a[i] = 1 << (s[i] - 'a');
        base[0] = a[0];
        vector<int> stack{0};
        int t = 0;
        while (!stack.empty()) {
            int u = stack.back();
            stack.pop_back();
            if (u >= 0) {
                tin[u] = ++t;
                order[t - 1] = u;
                stack.push_back(~u);
                for (int e = head[u]; e >= 0; e = nxt[e]) {
                    int v = to[e];
                    if (v != up[u]) {
                        up[v] = u;
                        base[v] = base[u] ^ a[v];
                        stack.push_back(v);
                    }
                }
            } else {
                tout[~u] = t;
            }
        }
        int LOG = 1;
        while ((1 << LOG) <= n) LOG++;
        vector<vector<int>> table(LOG, vector<int>(n));
        for (int i = 1; i < n; i++) table[0][i] = tin[up[order[i]]];
        for (int j = 1; (1 << j) <= n; j++)
            for (int i = 0; i + (1 << j) <= n; i++)
                table[j][i] = min(table[j - 1][i], table[j - 1][i + (1 << (j - 1))]);
        vector<int> bit(n + 2, 0);
        int size = n + 1;
        vector<bool> ans;
        for (auto& q : queries) {
            if (q[0] == 'u') {
                size_t sp = q.find(' ', 7);
                int u = stoi(q.substr(7, sp - 7));
                int m = a[u] ^ (1 << (q[sp + 1] - 'a'));
                if (m) {
                    a[u] ^= m;
                    for (int i = tin[u]; i <= size; i += i & -i) bit[i] ^= m;
                    for (int i = tout[u] + 1; i <= size; i += i & -i) bit[i] ^= m;
                }
            } else {
                size_t sp = q.find(' ', 6);
                int u = stoi(q.substr(6, sp - 6)), v = stoi(q.substr(sp + 1));
                int l = tin[u], r = tin[v];
                if (l > r) swap(l, r);
                int w;
                if (l == r) w = u;
                else {
                    int k = 31 - __builtin_clz(r - l);
                    w = order[min(table[k][l], table[k][r - (1 << k)]) - 1];
                }
                int m = base[u] ^ base[v] ^ a[w];
                for (int i = tin[u]; i; i &= i - 1) m ^= bit[i];
                for (int i = tin[v]; i; i &= i - 1) m ^= bit[i];
                ans.push_back((m & (m - 1)) == 0);
            }
        }
        return ans;
    }
};
