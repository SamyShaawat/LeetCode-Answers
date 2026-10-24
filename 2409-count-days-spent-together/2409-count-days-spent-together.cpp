class Solution {
public:
    int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        static const int c[12] = {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334};
        const string& s = max(arriveAlice, arriveBob);
        const string& e = min(leaveAlice, leaveBob);
        if (s > e) return 0;
        return c[(e[0] - '0') * 10 + e[1] - '0' - 1] + (e[3] - '0') * 10 + e[4] - '0'
             - c[(s[0] - '0') * 10 + s[1] - '0' - 1] - (s[3] - '0') * 10 - s[4] + '0' + 1;
    }
};
