class Solution {
public:
    int shortestPath(int n, vector<vector<int>>& edges, string labels, int k) {
        int K = k + 1, m = edges.size();
        vector<int> head(n + 1, 0), to(m), wt(m);
        for (auto& e : edges) head[e[0] + 1]++;
        for (int i = 0; i < n; i++) head[i + 1] += head[i];
        vector<int> pos(head.begin(), head.end() - 1);
        for (auto& e : edges) {
            int p = pos[e[0]]++;
            to[p] = e[1];
            wt[p] = e[2];
        }
        vector<int> dist(n * K, INT_MAX), minc(n, K);
        dist[1] = 0;
        priority_queue<long long, vector<long long>, greater<long long>> pq;
        pq.push(1);
        const long long mask = (1 << 22) - 1;
        while (!pq.empty()) {
            long long x = pq.top();
            pq.pop();
            int s = x & mask, d = x >> 22;
            if (d > dist[s]) continue;
            int u = s / K, c = s - u * K;
            if (c >= minc[u]) continue;
            if (u == n - 1) return d;
            minc[u] = c;
            for (int i = head[u]; i < head[u + 1]; i++) {
                int v = to[i], nc;
                if (labels[v] == labels[u]) {
                    nc = c + 1;
                    if (nc >= minc[v]) continue;
                } else {
                    if (minc[v] == 1) continue;
                    nc = 1;
                }
                int t = v * K + nc, nd = d + wt[i];
                if (nd < dist[t]) {
                    dist[t] = nd;
                    pq.push(((long long)nd << 22) | t);
                }
            }
        }
        return -1;
    }
};
