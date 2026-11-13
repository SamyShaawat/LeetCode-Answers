class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = [0] * (n + 1)
        top = -1
        h = 0
        cost = 0
        r = n - 1
        ans = 0
        for l in range(n - 1, -1, -1):
            x = nums[l]
            while top >= h and nums[st[top]] <= x:
                j = st[top]
                top -= 1
                cost += (x - nums[j]) * ((st[top] if top >= h else r + 1) - j)
            top += 1
            st[top] = l
            while cost > k:
                b = st[h]
                cost -= nums[b] - nums[r]
                if b == r:
                    h += 1
                r -= 1
            ans += r - l + 1
        return ans
