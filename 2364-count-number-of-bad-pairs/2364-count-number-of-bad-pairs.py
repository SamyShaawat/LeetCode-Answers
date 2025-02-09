class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        total_pairs = 0
        hashmap = {}
        for i in range(len(nums)):
            total_pairs += i
            good_pairs += hashmap.get(nums[i]-i,0)
            hashmap[nums[i]-i] = hashmap.get(nums[i]-i,0)+1
        return total_pairs - good_pairs