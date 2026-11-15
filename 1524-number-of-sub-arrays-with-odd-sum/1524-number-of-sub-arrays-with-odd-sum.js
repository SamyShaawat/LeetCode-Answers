/**
 * @param {number[]} arr
 * @return {number}
 */
var numOfSubarrays = function(arr) {
    let odd = 0, p = 0;
    for (let i = 0, n = arr.length; i < n; i++) {
        p ^= arr[i] & 1;
        odd += p;
    }
    return Number(BigInt(odd) * BigInt(arr.length + 1 - odd) % 1000000007n);
};
