class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord("a")] += 1
        for round in range(t):
            nxt = [0] * 26
            nxt[0] = cnt[25]
            nxt[1] = (cnt[25] + cnt[0]) % mod
            for i in range(2, 26):
                nxt[i] = cnt[i - 1]
            cnt = nxt
        ans = sum(cnt) % mod
        return ans