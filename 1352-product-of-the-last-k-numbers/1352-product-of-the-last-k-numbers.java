class ProductOfNumbers {
    private final int[] p = new int[40001];
    private int n = 1;

    public ProductOfNumbers() { p[0] = 1; }

    public void add(int num) {
        if (num == 0) n = 1;
        else { p[n] = p[n - 1] * num; n++; }
    }

    public int getProduct(int k) {
        return k >= n ? 0 : p[n - 1] / p[n - 1 - k];
    }
}
