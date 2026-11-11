class Solution {
public:
    long long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        long long m = min(need1, need2);
        return m * min(costBoth, cost1 + cost2) + (need1 - m) * min(costBoth, cost1) + (need2 - m) * min(costBoth, cost2);
    }
};
