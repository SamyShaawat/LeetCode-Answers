class Solution {
public:
    int closedIsland(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size(), res = 0;
        vector<pair<int,int>> st;
        for (int i = 1; i < m - 1; i++) {
            for (int j = 1; j < n - 1; j++) {
                if (grid[i][j] != 0) continue;
                grid[i][j] = 1;
                st.clear();
                st.push_back({i, j});
                int ok = 1;
                while (!st.empty()) {
                    auto [x, y] = st.back();
                    st.pop_back();
                    if (x == 0 || y == 0 || x == m - 1 || y == n - 1) {
                        ok = 0;
                        continue;
                    }
                    if (grid[x + 1][y] == 0) { grid[x + 1][y] = 1; st.push_back({x + 1, y}); }
                    if (grid[x - 1][y] == 0) { grid[x - 1][y] = 1; st.push_back({x - 1, y}); }
                    if (grid[x][y + 1] == 0) { grid[x][y + 1] = 1; st.push_back({x, y + 1}); }
                    if (grid[x][y - 1] == 0) { grid[x][y - 1] = 1; st.push_back({x, y - 1}); }
                }
                res += ok;
            }
        }
        return res;
    }
};
