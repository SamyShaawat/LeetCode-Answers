/**
 * @param {number[]} nums
 * @return {number}
 */
var minMoves2 = function(nums) {
    const n = nums.length;
    const a = Int32Array.from(nums);
    let lo = 0, hi = n - 1;
    const k = n >> 1;
    while (lo < hi) {
        const p = a[(lo + hi) >>> 1];
        let i = lo, j = hi;
        while (i <= j) {
            while (a[i] < p) i++;
            while (a[j] > p) j--;
            if (i <= j) {
                const t = a[i]; a[i] = a[j]; a[j] = t;
                i++; j--;
            }
        }
        if (k <= j) hi = j;
        else if (k >= i) lo = i;
        else break;
    }
    const med = a[k];
    let ans = 0;
    for (let x = 0; x < n; x++) ans += Math.abs(a[x] - med);
    return ans;
};
