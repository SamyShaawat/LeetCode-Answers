class Solution {
public:
    int smallestUniqueSubarray(vector<int>& nums) {
        typedef unsigned long long u64;
        const u64 M = (1ULL << 61) - 1, B = 100003;
        auto mul = [&](u64 a, u64 b) -> u64 {
            unsigned __int128 p = (unsigned __int128)a * b;
            u64 r = (u64)(p & M) + (u64)(p >> 61);
            return r >= M ? r - M : r;
        };
        int n = nums.size();
        vector<u64> H(n + 1, 0);
        for (int i = 0; i < n; i++) {
            u64 r = mul(H[i], B) + nums[i];
            H[i + 1] = r >= M ? r - M : r;
        }
        vector<u64> v;
        v.reserve(n);
        auto ok = [&](int L) {
            u64 P = 1, b = B;
            for (int e = L; e; e >>= 1, b = mul(b, b)) if (e & 1) P = mul(P, b);
            v.clear();
            for (int i = 0; i + L <= n; i++) {
                u64 s = mul(H[i], P);
                v.push_back(H[i + L] >= s ? H[i + L] - s : H[i + L] + M - s);
            }
            sort(v.begin(), v.end());
            int m = v.size();
            for (int i = 0, j; i < m; i = j) {
                for (j = i + 1; j < m && v[j] == v[i]; j++);
                if (j - i == 1) return true;
            }
            return false;
        };
        int lo = 1, hi = n;
        while (lo < hi) {
            int L = (lo + hi) >> 1;
            if (ok(L)) hi = L; else lo = L + 1;
        }
        return lo;
    }
};
