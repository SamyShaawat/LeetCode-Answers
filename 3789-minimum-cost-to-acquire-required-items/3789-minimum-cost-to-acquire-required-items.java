class Solution {
    public long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        long m = Math.min(need1, need2);
        return m * Math.min(costBoth, cost1 + cost2) + (need1 - m) * Math.min(costBoth, cost1) + (need2 - m) * Math.min(costBoth, cost2);
    }
}
