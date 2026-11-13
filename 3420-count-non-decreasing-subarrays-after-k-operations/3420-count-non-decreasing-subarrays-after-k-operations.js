/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countNonDecreasingSubarrays = function(nums, k) {
    const n = nums.length;
    const st = new Int32Array(n + 1);
    let top = -1, h = 0, r = n - 1, cost = 0, ans = 0;
    for (let l = n - 1; l >= 0; --l) {
        const x = nums[l];
        while (top >= h && nums[st[top]] <= x) {
            const j = st[top--];
            cost += (x - nums[j]) * ((top >= h ? st[top] : r + 1) - j);
        }
        st[++top] = l;
        while (cost > k) {
            const b = st[h];
            cost -= nums[b] - nums[r];
            if (b === r) ++h;
            --r;
        }
        ans += r - l + 1;
    }
    return ans;
};
