class Solution {
    public int sortPermutation(int[] nums) {
        int k = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i) {
                k &= nums[i];
                if (k == 0) return 0;
            }
        }
        return Math.max(k, 0);
    }
}
