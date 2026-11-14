var minimumSumSubarray = function(nums, l, r) {
    const n = nums.length;
    const p = new Array(n + 1);
    p[0] = 0;
    for (let i = 0; i < n; i++) p[i + 1] = p[i] + nums[i];
    let best = 1e9;
    for (let i = l; i <= n; i++) {
        const pi = p[i];
        for (let j = Math.max(0, i - r); j <= i - l; j++) {
            const s = pi - p[j];
            if (s > 0 && s < best) {
                if (s === 1) return 1;
                best = s;
            }
        }
    }
    return best === 1e9 ? -1 : best;
};
