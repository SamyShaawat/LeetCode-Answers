class Solution {
public:
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        int n = arrival.size();
        priority_queue<long long, vector<long long>, greater<long long>> busy;
        vector<int> cnt(k, 0);
        vector<int> init(k);
        for (int i = 0; i < k; i++) init[i] = i;
        priority_queue<int, vector<int>, greater<int>> free_(greater<int>(), move(init));
        for (int i = 0; i < n; i++) {
            long long a = arrival[i];
            while (!busy.empty() && (busy.top() >> 17) <= a) {
                int s = (int)(busy.top() & 131071);
                busy.pop();
                free_.push(i + ((s - i) % k + k) % k);
            }
            if (free_.empty()) continue;
            while (free_.top() < i) {
                int v = free_.top();
                free_.pop();
                free_.push(v + ((i - v + k - 1) / k) * k);
            }
            int s = free_.top() % k;
            free_.pop();
            cnt[s]++;
            busy.push(((a + load[i]) << 17) | s);
        }
        int m = *max_element(cnt.begin(), cnt.end());
        vector<int> res;
        for (int i = 0; i < k; i++) if (cnt[i] == m) res.push_back(i);
        return res;
    }
};
