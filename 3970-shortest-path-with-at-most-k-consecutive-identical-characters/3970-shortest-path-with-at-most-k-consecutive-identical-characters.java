class Solution {
    public int shortestPath(int n, int[][] edges, String labels, int k) {
        int K = k + 1, m = edges.length;
        int[] head = new int[n + 1], to = new int[m], wt = new int[m];
        for (int[] e : edges) head[e[0] + 1]++;
        for (int i = 0; i < n; i++) head[i + 1] += head[i];
        int[] pos = java.util.Arrays.copyOf(head, n);
        for (int[] e : edges) {
            int p = pos[e[0]]++;
            to[p] = e[1];
            wt[p] = e[2];
        }
        char[] lab = labels.toCharArray();
        int[] dist = new int[n * K], minc = new int[n];
        java.util.Arrays.fill(dist, Integer.MAX_VALUE);
        java.util.Arrays.fill(minc, K);
        dist[1] = 0;
        java.util.PriorityQueue<Long> pq = new java.util.PriorityQueue<>();
        pq.add(1L);
        long mask = (1L << 22) - 1;
        while (!pq.isEmpty()) {
            long x = pq.poll();
            int s = (int) (x & mask), d = (int) (x >> 22);
            if (d > dist[s]) continue;
            int u = s / K, c = s - u * K;
            if (c >= minc[u]) continue;
            if (u == n - 1) return d;
            minc[u] = c;
            for (int i = head[u]; i < head[u + 1]; i++) {
                int v = to[i], nc;
                if (lab[v] == lab[u]) {
                    nc = c + 1;
                    if (nc >= minc[v]) continue;
                } else {
                    if (minc[v] == 1) continue;
                    nc = 1;
                }
                int t = v * K + nc, nd = d + wt[i];
                if (nd < dist[t]) {
                    dist[t] = nd;
                    pq.add(((long) nd << 22) | t);
                }
            }
        }
        return -1;
    }
}
