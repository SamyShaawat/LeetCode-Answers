class Solution {
    public int minMoves2(int[] nums) {
        int n = nums.length;
        int lo = 0, hi = n - 1, k = n / 2;
        while (lo < hi) {
            int p = nums[(lo + hi) >>> 1], i = lo, j = hi;
            while (i <= j) {
                while (nums[i] < p) i++;
                while (nums[j] > p) j--;
                if (i <= j) {
                    int t = nums[i]; nums[i] = nums[j]; nums[j] = t;
                    i++; j--;
                }
            }
            if (k <= j) hi = j;
            else if (k >= i) lo = i;
            else break;
        }
        long med = nums[k], ans = 0;
        for (int x : nums) ans += Math.abs(x - med);
        return (int) ans;
    }
}
