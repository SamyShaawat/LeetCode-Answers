class ProductOfNumbers {
    vector<int> p{1};
public:
    ProductOfNumbers() { p.reserve(40001); }

    void add(int num) {
        if (num) p.push_back(p.back() * num);
        else p.assign(1, 1);
    }

    int getProduct(int k) {
        int n = p.size();
        return k >= n ? 0 : p[n - 1] / p[n - 1 - k];
    }
};
