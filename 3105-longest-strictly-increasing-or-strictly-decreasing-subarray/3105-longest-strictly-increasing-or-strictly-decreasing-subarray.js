/**
 * @param {number[]} nums
 * @return {number}
 */
var longestMonotonicSubarray = function(nums) {
    let best = 1, inc = 1, dec = 1, p = nums[0];
    for (let i = 0; i < nums.length; i++) {
        const x = nums[i];
        if (x > p) { inc++; dec = 1; }
        else if (x < p) { dec++; inc = 1; }
        else { inc = 1; dec = 1; }
        if (inc > best) best = inc;
        if (dec > best) best = dec;
        p = x;
    }
    return best;
};
