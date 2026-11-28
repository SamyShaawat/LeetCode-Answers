class Solution {
public:
    int maximumSaleItems(vector<vector<int>>& items, int budget) {
        int n = items.size();
        vector<int> cnt(n + 1, 0), D(n + 1, -1);
        long long m = LLONG_MAX;
        for (auto& it : items) {
            cnt[it[0]]++;
            m = min(m, (long long)it[1]);
        }
        for (int v = 1; v <= n; v++) {
            if (!cnt[v]) continue;
            int s = 0;
            for (int w = v; w <= n; w += v) s += cnt[w];
            D[v] = s - 1;
        }
        long long lim = 2 * m;
        vector<pair<long long, int>> groups;
        groups.reserve(n);
        for (auto& it : items)
            if (it[1] <= lim && D[it[0]] > 0) groups.push_back({it[1], D[it[0]]});
        sort(groups.begin(), groups.end());
        long long t = 0, R = budget;
        for (auto& [c, k] : groups) {
            long long x = R / c;
            if (x < k) {
                t += x;
                R -= x * c;
                break;
            }
            t += k;
            R -= k * c;
        }
        return (int)(2 * t + R / m);
    }
};
