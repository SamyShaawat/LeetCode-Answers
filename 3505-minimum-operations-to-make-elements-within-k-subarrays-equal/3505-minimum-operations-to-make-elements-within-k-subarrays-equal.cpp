class Solution {
public:
    long long minOperations(vector<int>& nums, int x, int k) {
        int n = nums.size(), m = n - x + 1;
        vector<int> id(n);
        iota(id.begin(), id.end(), 0);
        sort(id.begin(), id.end(), [&](int a, int b) {
            return nums[a] < nums[b] || (nums[a] == nums[b] && a < b);
        });
        vector<int> rk(n), sv(n);
        for (int r = 0; r < n; r++) { rk[id[r]] = r + 1; sv[r] = nums[id[r]]; }
        vector<int> cnt(n + 1, 0);
        vector<long long> sm(n + 1, 0);
        int top = 1;
        while (top * 2 <= n) top *= 2;
        auto upd = [&](int p, int c, long long v) {
            for (; p <= n; p += p & -p) { cnt[p] += c; sm[p] += v; }
        };
        long long tot = 0;
        for (int i = 0; i < x; i++) { upd(rk[i], 1, nums[i]); tot += nums[i]; }
        int h = (x + 1) / 2;
        vector<long long> cost(m);
        for (int i = 0; i < m; i++) {
            int pos = 0, rem = h;
            long long acc = 0;
            for (int pw = top; pw; pw >>= 1) {
                int q = pos + pw;
                if (q <= n && cnt[q] < rem) { pos = q; rem -= cnt[q]; acc += sm[q]; }
            }
            long long med = sv[pos], left = acc + med;
            cost[i] = med * h - left + (tot - left) - med * (x - h);
            if (i + 1 < m) {
                upd(rk[i], -1, -nums[i]);
                upd(rk[i + x], 1, nums[i + x]);
                tot += nums[i + x] - nums[i];
            }
        }
        const long long INF = LLONG_MAX / 4;
        vector<long long> prev(n + 1, 0), cur(n + 1);
        for (int j = 1; j <= k; j++) {
            fill(cur.begin(), cur.end(), INF);
            long long best = INF;
            for (int i = j * x; i <= n; i++) {
                best = min(best, prev[i - x] + cost[i - x]);
                cur[i] = best;
            }
            swap(prev, cur);
        }
        return prev[n];
    }
};
