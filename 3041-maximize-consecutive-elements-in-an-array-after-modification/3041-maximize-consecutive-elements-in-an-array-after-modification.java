class Solution {
    public int maxSelectedElements(int[] nums) {
        Arrays.sort(nums);
        int p = -2, a = 0, b = 0, best = 0;
        for (int x : nums) {
            if (x == p) {
                b = a + 1;
                best = Math.max(best, b);
                continue;
            }
            int m, d;
            if (x == p + 1) { m = a; d = b; }
            else if (x == p + 2) { m = b; d = 0; }
            else { m = 0; d = 0; }
            a = m + 1;
            b = d + 1;
            best = Math.max(best, Math.max(a, b));
            p = x;
        }
        return best;
    }
}