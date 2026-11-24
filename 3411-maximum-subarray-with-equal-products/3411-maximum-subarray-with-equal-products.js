/**
 * @param {number[]} nums
 * @return {number}
 */
var maxLength = function(nums) {
    const m = [0, 0, 1, 2, 1, 4, 3, 8, 1, 2, 5]; // prime bitmask
    let best = 2, l = 0, cur = 0;
    for (let r = 0; r < nums.length; ++r) {
        const b = m[nums[r]];
        while (cur & b) cur ^= m[nums[l++]];
        cur |= b;
        best = Math.max(best, r - l + 1);
    }
    return best;
};
