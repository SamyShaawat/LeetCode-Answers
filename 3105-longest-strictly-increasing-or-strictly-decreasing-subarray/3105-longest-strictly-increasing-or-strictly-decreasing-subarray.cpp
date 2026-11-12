class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int best = 1, inc = 1, dec = 1, p = nums[0];
        for (int x : nums) {
            if (x > p) { ++inc; dec = 1; }
            else if (x < p) { ++dec; inc = 1; }
            else { inc = dec = 1; }
            if (inc > best) best = inc;
            if (dec > best) best = dec;
            p = x;
        }
        return best;
    }
};
