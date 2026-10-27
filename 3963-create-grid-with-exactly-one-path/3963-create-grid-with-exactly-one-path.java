class Solution {
    public String[] createGrid(int m, int n) {
        String[] r = new String[m];
        String row = "#".repeat(n - 1) + ".";
        for (int i = 1; i < m; i++) r[i] = row;
        r[0] = ".".repeat(n);
        return r;
    }
}
