class Solution {
public:
    int maxSelectedElements(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int p = -2, a = 0, b = 0, best = 0;
        for (int x : nums) {
            if (x == p) {
                b = a + 1;
                best = max(best, b);
                continue;
            }
            int m, d;
            if (x == p + 1) { m = a; d = b; }
            else if (x == p + 2) { m = b; d = 0; }
            else { m = 0; d = 0; }
            a = m + 1;
            b = d + 1;
            best = max(best, max(a, b));
            p = x;
        }
        return best;
    }
};