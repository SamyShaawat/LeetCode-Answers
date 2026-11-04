var minOperations = function(nums, x, k) {
    const n = nums.length;
    const O = 1000000, B = 131072;
    // lo: max-heap of keys (stored negated in a min-heap); hi: min-heap of keys
    const lo = [], hi = [];
    const push = (h, v) => {
        let i = h.length;
        h.push(v);
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (h[p] <= v) break;
            h[i] = h[p];
            i = p;
        }
        h[i] = v;
    };
    const pop = (h) => {
        const top = h[0];
        const last = h.pop();
        const m = h.length;
        if (m > 0) {
            let i = 0;
            for (;;) {
                let l = 2 * i + 1;
                if (l >= m) break;
                if (l + 1 < m && h[l + 1] < h[l]) l++;
                if (h[l] >= last) break;
                h[i] = h[l];
                i = l;
            }
            h[i] = last;
        }
        return top;
    };
    const side = new Uint8Array(n);
    let ls = 0, hs = 0, lc = 0, hc = 0;
    const c = new Array(n);
    for (let i = 0; i < n; i++) {
        const v = nums[i];
        const key = (v + O) * B + i;
        if (lo.length && key < -lo[0]) { push(lo, -key); ls += v; lc++; side[i] = 1; }
        else { push(hi, key); hs += v; hc++; }
        const lim = i - x;
        if (i >= x) {
            const u = nums[lim];
            if (side[lim]) { lc--; ls -= u; }
            else { hc--; hs -= u; }
            while (lo.length && (-lo[0]) % B <= lim) pop(lo);
            while (hi.length && hi[0] % B <= lim) pop(hi);
        }
        while (lc > hc + 1) {
            const t = -pop(lo); lc--;
            const tv = Math.floor(t / B) - O;
            ls -= tv; push(hi, t); hc++; hs += tv; side[t % B] = 0;
            while (lo.length && (-lo[0]) % B <= lim) pop(lo);
        }
        while (lc < hc) {
            const t = pop(hi); hc--;
            const tv = Math.floor(t / B) - O;
            hs -= tv; push(lo, -t); lc++; ls += tv; side[t % B] = 1;
            while (hi.length && hi[0] % B <= lim) pop(hi);
        }
        if (i >= x - 1) {
            const m = Math.floor(-lo[0] / B) - O;
            c[i - x + 1] = m * lc - ls + hs - m * hc;
        }
    }
    const INF = 1e18;
    let prev = new Array(n + 1).fill(0);
    let cur = new Array(n + 1);
    for (let j = 1; j <= k; j++) {
        cur.fill(INF);
        for (let i = j * x; i <= n; i++) {
            const a = prev[i - x] + c[i - x];
            const b = cur[i - 1];
            cur[i] = a < b ? a : b;
        }
        const t = prev; prev = cur; cur = t;
    }
    return prev[n];
};
