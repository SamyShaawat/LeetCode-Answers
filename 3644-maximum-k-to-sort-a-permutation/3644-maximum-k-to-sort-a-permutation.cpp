class Solution {
public:
    int sortPermutation(vector<int>& nums) {
        int k = -1;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (nums[i] != i) {
                k &= nums[i];
                if (!k) return 0;
            }
        }
        return max(k, 0);
    }
};
