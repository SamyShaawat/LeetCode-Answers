class Solution {
public:
    int minChanges(string s) {
        int r = 0;
        for (int i = 0; i < (int)s.size(); i += 2) r += s[i] != s[i + 1];
        return r;
    }
};
