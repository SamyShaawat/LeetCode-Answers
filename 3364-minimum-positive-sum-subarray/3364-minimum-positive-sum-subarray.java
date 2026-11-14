class Solution {
    public int minimumSumSubarray(List<Integer> nums, int l, int r) {
        int n = nums.size(), best = Integer.MAX_VALUE;
        int[] p = new int[n + 1];
        for (int i = 0; i < n; i++) p[i + 1] = p[i] + nums.get(i);
        for (int i = l; i <= n; i++) {
            int pi = p[i];
            for (int j = Math.max(0, i - r); j <= i - l; j++) {
                int s = pi - p[j];
                if (s > 0 && s < best) {
                    if (s == 1) return 1;
                    best = s;
                }
            }
        }
        return best == Integer.MAX_VALUE ? -1 : best;
    }
}
