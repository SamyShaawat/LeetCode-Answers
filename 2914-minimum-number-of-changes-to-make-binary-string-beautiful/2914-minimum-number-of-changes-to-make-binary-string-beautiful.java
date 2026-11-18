class Solution {
    public int minChanges(String s) {
        int r = 0;
        for (int i = 0, n = s.length(); i < n; i += 2) if (s.charAt(i) != s.charAt(i + 1)) r++;
        return r;
    }
}
