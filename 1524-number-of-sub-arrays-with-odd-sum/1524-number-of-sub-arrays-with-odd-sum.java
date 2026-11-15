class Solution {
    public int numOfSubarrays(int[] arr) {
        int odd = 0, p = 0;
        for (int x : arr) {
            p ^= x & 1;
            odd += p;
        }
        return (int) ((long) odd * (arr.length + 1 - odd) % 1000000007);
    }
}
