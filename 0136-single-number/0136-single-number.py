class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        print(hashmap)
        for key, value in hashmap.items():
            if value == 1:
                return key
        