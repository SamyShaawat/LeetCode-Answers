class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size(), top = -1, h = 0, r = n - 1;
        vector<int> st(n + 1);
        long long cost = 0, ans = 0;
        for (int l = n - 1; l >= 0; --l) {
            int x = nums[l];
            while (top >= h && nums[st[top]] <= x) {
                int j = st[top--];
                int nxt = top >= h ? st[top] : r + 1;
                cost += (long long)(x - nums[j]) * (nxt - j);
            }
            st[++top] = l;
            while (cost > k) {
                int b = st[h];
                cost -= nums[b] - nums[r];
                if (b == r) ++h;
                --r;
            }
            ans += r - l + 1;
        }
        return ans;
    }
};
