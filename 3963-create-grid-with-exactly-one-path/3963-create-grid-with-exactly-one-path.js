var createGrid = function(m, n) {
    const r = new Array(m).fill("#".repeat(n - 1) + ".");
    r[0] = ".".repeat(n);
    return r;
};
