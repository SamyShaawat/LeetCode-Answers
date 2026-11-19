/**
 * @param {number[]} nums
 * @return {number}
 */
var minimizeSum = function(nums) {
    let a = Infinity, b = a, c = a, x = -Infinity, y = x, z = x;
    for (const v of nums) {
        if (v < a) { c = b; b = a; a = v; }
        else if (v < b) { c = b; b = v; }
        else if (v < c) c = v;
        if (v > x) { z = y; y = x; x = v; }
        else if (v > y) { z = y; y = v; }
        else if (v > z) z = v;
    }
    return Math.min(x - c, z - a, y - b);
};
