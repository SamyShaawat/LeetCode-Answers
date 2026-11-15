class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        int odd = 0, p = 0;
        for (int x : arr) {
            p ^= x & 1;
            odd += p;
        }
        return (long long)odd * (arr.size() + 1 - odd) % 1000000007;
    }
};
