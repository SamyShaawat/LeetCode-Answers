var ProductOfNumbers = function() {
    this.p = new Int32Array(40001);
    this.p[0] = 1;
    this.n = 1;
};

ProductOfNumbers.prototype.add = function(num) {
    if (num === 0) this.n = 1;
    else { this.p[this.n] = this.p[this.n - 1] * num; this.n++; }
};

ProductOfNumbers.prototype.getProduct = function(k) {
    const n = this.n;
    return k >= n ? 0 : (this.p[n - 1] / this.p[n - 1 - k]) | 0;
};
