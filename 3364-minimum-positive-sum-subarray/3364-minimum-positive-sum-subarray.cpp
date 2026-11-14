class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int n = nums.size(), best = INT_MAX;
        int p[101];
        p[0] = 0;
        for (int i = 0; i < n; i++) p[i + 1] = p[i] + nums[i];
        for (int i = l; i <= n; i++) {
            int pi = p[i];
            for (int j = max(0, i - r); j <= i - l; j++) {
                int s = pi - p[j];
                if (s > 0 && s < best) {
                    if (s == 1) return 1;
                    best = s;
                }
            }
        }
        return best == INT_MAX ? -1 : best;
    }
};
