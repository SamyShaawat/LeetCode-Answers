/**
 * @param {number} cost1
 * @param {number} cost2
 * @param {number} costBoth
 * @param {number} need1
 * @param {number} need2
 * @return {number}
 */
var minimumCost = function(cost1, cost2, costBoth, need1, need2) {
    const m = Math.min(need1, need2);
    return m * Math.min(costBoth, cost1 + cost2) + (need1 - m) * Math.min(costBoth, cost1) + (need2 - m) * Math.min(costBoth, cost2);
};
