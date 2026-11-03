class Solution {
public:
    int minMoves(vector<int>& nums) {
        int mx = 0, s = 0;
        for (int x : nums) { s += x; if (x > mx) mx = x; }
        return mx * (int)nums.size() - s;
    }
};
