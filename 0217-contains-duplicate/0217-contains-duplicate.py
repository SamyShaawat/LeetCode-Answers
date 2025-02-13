class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = Counter(nums)
        for value in hashmap.values():
            if value > 1:
                return True
        return False
        