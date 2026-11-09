/**
 * @param {number} k
 * @param {number[]} arrival
 * @param {number[]} load
 * @return {number[]}
 */
var busiestServers = function(k, arrival, load) {
    const n = arrival.length;
    const free = new Int32Array(k);
    for (let i = 0; i < k; i++) free[i] = i;
    let fs = k;
    const busy = new Float64Array(k);
    let bs = 0;
    const cnt = new Int32Array(k);
    for (let i = 0; i < n; i++) {
        const lim = (arrival[i] + 1) * 131072;
        while (bs > 0 && busy[0] < lim) {
            const s = busy[0] % 131072;
            const last = busy[--bs];
            let p = 0;
            while (true) {
                let c = 2 * p + 1;
                if (c >= bs) break;
                if (c + 1 < bs && busy[c + 1] < busy[c]) c++;
                if (busy[c] >= last) break;
                busy[p] = busy[c];
                p = c;
            }
            if (bs > 0) busy[p] = last;
            const v = i + (((s - i) % k) + k) % k;
            let q = fs++;
            while (q > 0) {
                const par = (q - 1) >> 1;
                if (free[par] <= v) break;
                free[q] = free[par];
                q = par;
            }
            free[q] = v;
        }
        if (fs === 0) continue;
        while (free[0] < i) {
            let v = free[0];
            v += Math.floor((i - v + k - 1) / k) * k;
            let p = 0;
            while (true) {
                let c = 2 * p + 1;
                if (c >= fs) break;
                if (c + 1 < fs && free[c + 1] < free[c]) c++;
                if (free[c] >= v) break;
                free[p] = free[c];
                p = c;
            }
            free[p] = v;
        }
        const s = free[0] % k;
        const last = free[--fs];
        let p = 0;
        while (true) {
            let c = 2 * p + 1;
            if (c >= fs) break;
            if (c + 1 < fs && free[c + 1] < free[c]) c++;
            if (free[c] >= last) break;
            free[p] = free[c];
            p = c;
        }
        if (fs > 0) free[p] = last;
        cnt[s]++;
        const e = (arrival[i] + load[i]) * 131072 + s;
        let q = bs++;
        while (q > 0) {
            const par = (q - 1) >> 1;
            if (busy[par] <= e) break;
            busy[q] = busy[par];
            q = par;
        }
        busy[q] = e;
    }
    let m = 0;
    for (let i = 0; i < k; i++) if (cnt[i] > m) m = cnt[i];
    const res = [];
    for (let i = 0; i < k; i++) if (cnt[i] === m) res.push(i);
    return res;
};
