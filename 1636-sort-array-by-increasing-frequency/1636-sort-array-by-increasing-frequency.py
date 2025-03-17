class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        nums.sort(key=lambda x: (hashmap[x], -x))
        return nums

        