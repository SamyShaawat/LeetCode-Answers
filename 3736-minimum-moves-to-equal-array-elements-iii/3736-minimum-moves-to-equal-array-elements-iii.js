/**
 * @param {number[]} nums
 * @return {number}
 */
var minMoves = function(nums) {
    let mx = 0, s = 0;
    for (const x of nums) { s += x; if (x > mx) mx = x; }
    return mx * nums.length - s;
};
