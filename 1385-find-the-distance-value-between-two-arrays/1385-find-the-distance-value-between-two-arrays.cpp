class Solution {
public:
    int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
        sort(arr2.begin(), arr2.end());
        int c = 0;
        for (int x : arr1) {
            auto it = lower_bound(arr2.begin(), arr2.end(), x - d);
            if (it == arr2.end() || *it > x + d) ++c;
        }
        return c;
    }
};
