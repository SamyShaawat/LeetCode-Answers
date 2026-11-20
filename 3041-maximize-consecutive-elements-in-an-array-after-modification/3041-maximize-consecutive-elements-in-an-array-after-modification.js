/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSelectedElements = function(nums) {
    const arr = Int32Array.from(nums).sort();
    let p = -2, a = 0, b = 0, best = 0;
    for (const x of arr) {
        if (x === p) {
            b = a + 1;
            if (b > best) best = b;
            continue;
        }
        let m, d;
        if (x === p + 1) { m = a; d = b; }
        else if (x === p + 2) { m = b; d = 0; }
        else { m = 0; d = 0; }
        a = m + 1;
        b = d + 1;
        best = Math.max(best, a, b);
        p = x;
    }
    return best;
};