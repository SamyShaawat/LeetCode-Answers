class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        bitset<1024> M[10];
        for (int b = 0; b < 10; b++)
            for (int x = 0; x < 1024; x++)
                if (!((x >> b) & 1)) M[b][x] = 1;
        int m = grid.size(), n = grid[0].size();
        vector<bitset<1024>> cur(n);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int g = grid[i][j];
                bitset<1024> s;
                if (i == 0 && j == 0) {
                    s[g] = 1;
                } else {
                    if (i == 0) s = cur[j - 1];
                    else if (j == 0) s = cur[0];
                    else s = cur[j] | cur[j - 1];
                    for (int b = 0; b < 10; b++)
                        if ((g >> b) & 1) {
                            int w = 1 << b;
                            s = ((s & M[b]) << w) | ((s >> w) & M[b]);
                        }
                }
                cur[j] = s;
            }
        }
        return cur[n - 1]._Find_first();
    }
};
