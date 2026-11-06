class Solution {
public:
    vector<int> countServers(int n, vector<vector<int>>& logs, int x, vector<int>& queries) {
        sort(logs.begin(), logs.end(), [](const vector<int>& a, const vector<int>& b) { return a[1] < b[1]; });
        int k = queries.size();
        vector<int> order(k);
        iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(), [&](int a, int b) { return queries[a] < queries[b]; });
        vector<int> cnt(n + 1, 0), res(k);
        int m = logs.size(), lo = 0, hi = 0, active = 0;
        for (int qi : order) {
            int q = queries[qi], left = q - x;
            while (hi < m && logs[hi][1] <= q) {
                if (cnt[logs[hi][0]]++ == 0) active++;
                hi++;
            }
            while (lo < hi && logs[lo][1] < left) {
                if (--cnt[logs[lo][0]] == 0) active--;
                lo++;
            }
            res[qi] = n - active;
        }
        return res;
    }
};
