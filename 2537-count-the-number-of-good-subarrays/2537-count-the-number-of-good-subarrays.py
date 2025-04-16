class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        res = 0 
        left = 0 
        pairs = 0
        counter = Counter()
        n = len(nums)
        for right in range(n):
            pairs += counter[nums[right]]
            counter[nums[right]] += 1
            while pairs >= k:
                counter[nums[left]] -= 1
                pairs -= counter[nums[left]]
                left +=1
            res += left
        return res 
        