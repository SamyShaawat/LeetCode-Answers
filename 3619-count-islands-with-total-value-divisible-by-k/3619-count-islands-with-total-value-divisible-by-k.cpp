class Solution {
public:
    int countIslands(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size(), ans = 0;
        vector<int> st;
        st.reserve(m * n);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!grid[i][j]) continue;
                long long s = grid[i][j];
                grid[i][j] = 0;
                st.push_back(i * n + j);
                while (!st.empty()) {
                    int p = st.back();
                    st.pop_back();
                    int r = p / n, c = p % n;
                    if (r > 0 && grid[r - 1][c]) { s += grid[r - 1][c]; grid[r - 1][c] = 0; st.push_back(p - n); }
                    if (r + 1 < m && grid[r + 1][c]) { s += grid[r + 1][c]; grid[r + 1][c] = 0; st.push_back(p + n); }
                    if (c > 0 && grid[r][c - 1]) { s += grid[r][c - 1]; grid[r][c - 1] = 0; st.push_back(p - 1); }
                    if (c + 1 < n && grid[r][c + 1]) { s += grid[r][c + 1]; grid[r][c + 1] = 0; st.push_back(p + 1); }
                }
                if (s % k == 0) ans++;
            }
        }
        return ans;
    }
};
