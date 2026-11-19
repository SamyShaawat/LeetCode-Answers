class Solution {
public:
    int minimizeSum(vector<int>& nums) {
        int a = INT_MAX, b = INT_MAX, c = INT_MAX, x = INT_MIN, y = INT_MIN, z = INT_MIN;
        for (int v : nums) {
            if (v < a) { c = b; b = a; a = v; }
            else if (v < b) { c = b; b = v; }
            else if (v < c) c = v;
            if (v > x) { z = y; y = x; x = v; }
            else if (v > y) { z = y; y = v; }
            else if (v > z) z = v;
        }
        return min({x - c, z - a, y - b});
    }
};
