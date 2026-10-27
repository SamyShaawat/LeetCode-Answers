class Solution {
public:
    vector<string> createGrid(int m, int n) {
        vector<string> r(m, string(n - 1, '#') + '.');
        r[0] = string(n, '.');
        return r;
    }
};
