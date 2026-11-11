class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if need1 > need2:
            cost1, cost2, need1, need2 = cost2, cost1, need2, need1
        both = costBoth if costBoth < cost1 + cost2 else cost1 + cost2
        rest = costBoth if costBoth < cost2 else cost2
        return need1 * both + (need2 - need1) * rest
