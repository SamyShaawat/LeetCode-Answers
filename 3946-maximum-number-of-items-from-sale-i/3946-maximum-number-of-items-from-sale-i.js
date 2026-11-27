/**
 * @param {number[][]} items
 * @param {number} budget
 * @return {number}
 */
var maximumSaleItems = function(items, budget) {
    let M = 0, pmin = Infinity;
    for (const [f, p] of items) { if (f > M) M = f; if (p < pmin) pmin = p; }
    const freq = new Int32Array(M + 1), cnt = new Int32Array(M + 1);
    for (const [f] of items) freq[f]++;
    for (let f = 1; f <= M; f++)
        if (freq[f])
            for (let m = f; m <= M; m += f) cnt[f] += freq[m];
    const dp = new Int32Array(budget + 1);
    for (const [f, p] of items) {
        const v = cnt[f];
        if (p > budget || v <= Math.floor(p / pmin)) continue;
        for (let b = budget; b >= p; b--) dp[b] = Math.max(dp[b], dp[b - p] + v);
    }
    let ans = 0;
    for (let b = 0; b <= budget; b++) ans = Math.max(ans, dp[b] + Math.floor((budget - b) / pmin));
    return ans;
};