class Solution {
    public int[] findSubtreeSizes(int[] parent, String s) {
        int n = parent.length;
        int[] head = new int[n], nxt = new int[n], np = parent.clone(), saved = new int[n], order = new int[n];
        java.util.Arrays.fill(head, -1);
        for (int i = n - 1; i > 0; --i) { nxt[i] = head[parent[i]]; head[parent[i]] = i; }
        char[] cs = s.toCharArray();
        int[] last = new int[26];
        java.util.Arrays.fill(last, -1);
        int[] st = new int[2 * n + 1];
        int top = 0, k = 0;
        st[top++] = 0;
        while (top > 0) {
            int u = st[--top];
            if (u >= 0) {
                int c = cs[u] - 'a';
                if (last[c] >= 0) np[u] = last[c];
                saved[u] = last[c]; last[c] = u;
                order[k++] = u;
                st[top++] = ~u;
                for (int v = head[u]; v != -1; v = nxt[v]) st[top++] = v;
            } else {
                int x = ~u; last[cs[x] - 'a'] = saved[x];
            }
        }
        int[] sz = new int[n];
        java.util.Arrays.fill(sz, 1);
        for (int i = n - 1; i > 0; --i) { int u = order[i]; sz[np[u]] += sz[u]; }
        return sz;
    }
}