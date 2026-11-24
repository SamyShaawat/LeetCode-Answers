class Solution {
public:
    int maxLength(vector<int>& nums) {
        static const int m[11] = {0, 0, 1, 2, 1, 4, 3, 8, 1, 2, 5}; // prime bitmask
        int best = 2, l = 0, cur = 0, n = nums.size();
        for (int r = 0; r < n; ++r) {
            int b = m[nums[r]];
            while (cur & b) cur ^= m[nums[l++]];
            cur |= b;
            best = max(best, r - l + 1);
        }
        return best;
    }
};
