/**
 * @param {number[]} nums
 * @return {number}
 */
var smallestUniqueSubarray = function(nums) {
    // two primes < 2^26: every product < 2^52 stays exact in a double
    const n = nums.length, M1 = 67108859, M2 = 67108837, B = 100003;
    const h1 = new Float64Array(n + 1), h2 = new Float64Array(n + 1);
    for (let i = 0; i < n; i++) {
        h1[i + 1] = (h1[i] * B + nums[i]) % M1;
        h2[i + 1] = (h2[i] * B + nums[i]) % M2;
    }
    const powmod = (e, m) => { let r = 1, b = B % m; for (; e; e >>= 1, b = b * b % m) if (e & 1) r = r * b % m; return r; };
    const v = new Float64Array(n);
    let lo = 1, hi = n;
    while (lo < hi) {
        const L = (lo + hi) >> 1, P1 = powmod(L, M1), P2 = powmod(L, M2), m = n - L + 1;
        for (let i = 0; i < m; i++) {
            const a = (h1[i + L] - h1[i] * P1 % M1 + M1) % M1;
            const b = (h2[i + L] - h2[i] * P2 % M2 + M2) % M2;
            v[i] = a * 67108864 + b;
        }
        const s = v.subarray(0, m).sort();
        let ok = false;
        for (let i = 0, j; i < m && !ok; i = j) {
            for (j = i + 1; j < m && s[j] === s[i]; j++);
            if (j - i === 1) ok = true;
        }
        if (ok) hi = L; else lo = L + 1;
    }
    return lo;
};
