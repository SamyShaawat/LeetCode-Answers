class Solution {
    public int minimizeSum(int[] nums) {
        int a = Integer.MAX_VALUE, b = a, c = a, x = Integer.MIN_VALUE, y = x, z = x;
        for (int v : nums) {
            if (v < a) { c = b; b = a; a = v; }
            else if (v < b) { c = b; b = v; }
            else if (v < c) c = v;
            if (v > x) { z = y; y = x; x = v; }
            else if (v > y) { z = y; y = v; }
            else if (v > z) z = v;
        }
        return Math.min(x - c, Math.min(z - a, y - b));
    }
}
