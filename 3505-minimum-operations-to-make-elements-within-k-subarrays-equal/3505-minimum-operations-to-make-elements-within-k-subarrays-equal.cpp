class Solution {
public:
    long long minOperations(vector<int>& nums, int x, int k) {
        int n = nums.size();
        const int O = 1000000, SH = 17;
        const long long M = (1LL << SH) - 1;
        priority_queue<long long> lo;
        priority_queue<long long, vector<long long>, greater<long long>> hi;
        vector<char> side(n, 0);
        long long ls = 0, hs = 0;
        int lc = 0, hc = 0;
        vector<long long> c;
        c.reserve(n);
        for (int i = 0; i < n; i++) {
            int v = nums[i];
            long long key = ((long long)(v + O) << SH) | i;
            if (!lo.empty() && key < lo.top()) { lo.push(key); ls += v; lc++; side[i] = 1; }
            else { hi.push(key); hs += v; hc++; }
            long long lim = i - x;
            if (i >= x) {
                int u = nums[lim];
                if (side[lim]) { lc--; ls -= u; }
                else { hc--; hs -= u; }
                while (!lo.empty() && (lo.top() & M) <= lim) lo.pop();
                while (!hi.empty() && (hi.top() & M) <= lim) hi.pop();
            }
            while (lc > hc + 1) {
                long long t = lo.top(); lo.pop(); lc--;
                long long tv = (t >> SH) - O;
                ls -= tv; hi.push(t); hc++; hs += tv; side[t & M] = 0;
                while (!lo.empty() && (lo.top() & M) <= lim) lo.pop();
            }
            while (lc < hc) {
                long long t = hi.top(); hi.pop(); hc--;
                long long tv = (t >> SH) - O;
                hs -= tv; lo.push(t); lc++; ls += tv; side[t & M] = 1;
                while (!hi.empty() && (hi.top() & M) <= lim) hi.pop();
            }
            if (i >= x - 1) {
                long long m = (lo.top() >> SH) - O;
                c.push_back(m * lc - ls + hs - m * hc);
            }
        }
        const long long INF = (long long)4e18;
        vector<long long> prev(n + 1, 0), cur(n + 1);
        for (int j = 1; j <= k; j++) {
            fill(cur.begin(), cur.end(), INF);
            for (int i = j * x; i <= n; i++) {
                long long a = prev[i - x] + c[i - x];
                long long b = cur[i - 1];
                cur[i] = a < b ? a : b;
            }
            swap(prev, cur);
        }
        return prev[n];
    }
};
