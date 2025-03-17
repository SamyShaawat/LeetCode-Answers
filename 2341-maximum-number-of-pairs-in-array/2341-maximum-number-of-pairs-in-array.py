class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        result = [0, 0]
        for key, value in hashmap.items():
            if value %2:
                result[1] += 1
            result[0] += value//2
        return result
        