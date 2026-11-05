/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @param {number} d
 * @return {number}
 */
var findTheDistanceValue = function(arr1, arr2, d) {
    const b = Int32Array.from(arr2).sort();
    const n = b.length;
    let c = 0;
    for (let k = 0; k < arr1.length; k++) {
        const x = arr1[k];
        let lo = 0, hi = n;
        const t = x - d;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (b[mid] < t) lo = mid + 1;
            else hi = mid;
        }
        if (lo === n || b[lo] > x + d) c++;
    }
    return c;
};
