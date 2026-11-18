/**
 * @param {string} s
 * @return {number}
 */
var minChanges = function(s) {
    let r = 0;
    for (let i = 0, n = s.length; i < n; i += 2) if (s[i] !== s[i + 1]) r++;
    return r;
};
