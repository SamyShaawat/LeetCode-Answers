class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = []
        h = 0
        cost = 0
        r = n - 1
        ans = 0
        for l in range(n - 1, -1, -1):
            x = nums[l]
            while len(st) > h and nums[st[-1]] <= x:
                j = st.pop()
                nxt = st[-1] if len(st) > h else r + 1
                cost += (x - nums[j]) * (nxt - j)
            st.append(l)
            while cost > k:
                b = st[h]
                cost -= nums[b] - nums[r]
                if b == r:
                    h += 1
                r -= 1
            ans += r - l + 1
        return ans
