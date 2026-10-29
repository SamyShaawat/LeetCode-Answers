class Solution {
    public List<Boolean> palindromePath(int n, int[][] edges, String s, String[] queries) {
        int[] head = new int[n], nxt = new int[2 * n], to = new int[2 * n];
        Arrays.fill(head, -1);
        int ec = 0;
        for (int[] e : edges) {
            to[ec] = e[1]; nxt[ec] = head[e[0]]; head[e[0]] = ec++;
            to[ec] = e[0]; nxt[ec] = head[e[1]]; head[e[1]] = ec++;
        }
        int[] cur = new int[n], par = new int[n], pre = new int[n], dep = new int[n], tin = new int[n], order = new int[n], sz = new int[n];
        for (int i = 0; i < n; i++) { cur[i] = 1 << (s.charAt(i) - 'a'); sz[i] = 1; }
        par[0] = -1;
        pre[0] = cur[0];
        int[] st = new int[n];
        int sp0 = 0, cnt = 0;
        st[sp0++] = 0;
        while (sp0 > 0) {
            int u = st[--sp0];
            tin[u] = cnt;
            order[cnt++] = u;
            for (int e = head[u]; e >= 0; e = nxt[e]) {
                int w = to[e];
                if (w != par[u]) {
                    par[w] = u;
                    dep[w] = dep[u] + 1;
                    pre[w] = pre[u] ^ cur[w];
                    st[sp0++] = w;
                }
            }
        }
        for (int i = n - 1; i > 0; i--) sz[par[order[i]]] += sz[order[i]];
        int LOG = 1;
        while ((1 << LOG) <= n) LOG++;
        long[][] sp = new long[LOG][n];
        for (int i = 0; i < n; i++) sp[0][i] = ((long) dep[order[i]] << 16) | par[order[i]];
        for (int k = 1; k < LOG; k++)
            for (int i = 0; i + (1 << k) <= n; i++)
                sp[k][i] = Math.min(sp[k - 1][i], sp[k - 1][i + (1 << (k - 1))]);
        int[] bit = new int[n + 2];
        List<Boolean> ans = new ArrayList<>();
        for (String q : queries) {
            int u = 0, p = q.indexOf(' ') + 1;
            while (q.charAt(p) != ' ') u = u * 10 + q.charAt(p++) - '0';
            p++;
            if (q.charAt(0) == 'u') {
                int c = 1 << (q.charAt(p) - 'a');
                int d = cur[u] ^ c;
                if (d != 0) {
                    cur[u] = c;
                    for (int i = tin[u] + 1; i <= n; i += i & -i) bit[i] ^= d;
                    for (int i = tin[u] + sz[u] + 1; i <= n; i += i & -i) bit[i] ^= d;
                }
            } else {
                int v = 0, len = q.length();
                while (p < len) v = v * 10 + q.charAt(p++) - '0';
                int x = pre[u] ^ pre[v];
                for (int i = tin[u] + 1; i != 0; i &= i - 1) x ^= bit[i];
                for (int i = tin[v] + 1; i != 0; i &= i - 1) x ^= bit[i];
                int lo = tin[u], hi = tin[v], l;
                if (lo > hi) { int t = lo; lo = hi; hi = t; }
                if (lo == hi) l = u;
                else {
                    lo++;
                    int k = 31 - Integer.numberOfLeadingZeros(hi - lo + 1);
                    l = (int) (Math.min(sp[k][lo], sp[k][hi - (1 << k) + 1]) & 65535);
                }
                x ^= cur[l];
                ans.add((x & (x - 1)) == 0);
            }
        }
        return ans;
    }
}
