class Solution {
    public List<Boolean> palindromePath(int n, int[][] edges, String s, String[] queries) {
        int[] head = new int[n], nxt = new int[2 * n], to = new int[2 * n];
        Arrays.fill(head, -1);
        int ec = 0;
        for (int[] e : edges) {
            to[ec] = e[1]; nxt[ec] = head[e[0]]; head[e[0]] = ec++;
            to[ec] = e[0]; nxt[ec] = head[e[1]]; head[e[1]] = ec++;
        }
        int[] a = new int[n], tin = new int[n], tout = new int[n], base = new int[n], order = new int[n], up = new int[n];
        for (int i = 0; i < n; i++) a[i] = 1 << (s.charAt(i) - 'a');
        up[0] = -1;
        base[0] = a[0];
        int[] stack = new int[2 * n];
        int sp = 0, t = 0;
        stack[sp++] = 0;
        while (sp > 0) {
            int u = stack[--sp];
            if (u >= 0) {
                tin[u] = ++t;
                order[t - 1] = u;
                stack[sp++] = ~u;
                for (int e = head[u]; e >= 0; e = nxt[e]) {
                    int v = to[e];
                    if (v != up[u]) {
                        up[v] = u;
                        base[v] = base[u] ^ a[v];
                        stack[sp++] = v;
                    }
                }
            } else {
                tout[~u] = t;
            }
        }
        int LOG = 32 - Integer.numberOfLeadingZeros(n);
        int[][] table = new int[LOG][n];
        for (int i = 1; i < n; i++) table[0][i] = tin[up[order[i]]];
        for (int j = 1; (1 << j) <= n; j++)
            for (int i = 0; i + (1 << j) <= n; i++)
                table[j][i] = Math.min(table[j - 1][i], table[j - 1][i + (1 << (j - 1))]);
        int[] bit = new int[n + 2];
        int size = n + 1;
        List<Boolean> ans = new ArrayList<>();
        for (String q : queries) {
            if (q.charAt(0) == 'u') {
                int p = q.indexOf(' ', 7);
                int u = Integer.parseInt(q.substring(7, p));
                int m = a[u] ^ (1 << (q.charAt(p + 1) - 'a'));
                if (m != 0) {
                    a[u] ^= m;
                    for (int i = tin[u]; i <= size; i += i & -i) bit[i] ^= m;
                    for (int i = tout[u] + 1; i <= size; i += i & -i) bit[i] ^= m;
                }
            } else {
                int p = q.indexOf(' ', 6);
                int u = Integer.parseInt(q.substring(6, p)), v = Integer.parseInt(q.substring(p + 1));
                int l = tin[u], r = tin[v];
                if (l > r) { int x = l; l = r; r = x; }
                int w;
                if (l == r) w = u;
                else {
                    int k = 31 - Integer.numberOfLeadingZeros(r - l);
                    w = order[Math.min(table[k][l], table[k][r - (1 << k)]) - 1];
                }
                int m = base[u] ^ base[v] ^ a[w];
                for (int i = tin[u]; i != 0; i &= i - 1) m ^= bit[i];
                for (int i = tin[v]; i != 0; i &= i - 1) m ^= bit[i];
                ans.add((m & (m - 1)) == 0);
            }
        }
        return ans;
    }
}
