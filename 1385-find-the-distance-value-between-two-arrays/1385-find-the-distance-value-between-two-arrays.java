class Solution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        Arrays.sort(arr2);
        int n = arr2.length, c = 0;
        for (int x : arr1) {
            int lo = 0, hi = n, t = x - d;
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;
                if (arr2[mid] < t) lo = mid + 1;
                else hi = mid;
            }
            if (lo == n || arr2[lo] > x + d) c++;
        }
        return c;
    }
}
