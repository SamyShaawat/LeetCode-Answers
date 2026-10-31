class Solution {
public:
    int uniquePaths(vector<vector<int>>& grid) {
        const int M = 1000000007;
        int n = grid[0].size();
        vector<int> b(n, 0), nb(n, 0);
        b[0] = 1;
        int t = 0;
        for (auto& row : grid) {
            int a = 0;
            for (int j = 0; j < n; j++) {
                if (row[j]) {
                    nb[j] = a;
                    a = b[j];
                } else {
                    t = (a + b[j]) % M;
                    a = nb[j] = t;
                }
            }
            swap(b, nb);
        }
        return t;
    }
};
