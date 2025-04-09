class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        print(hashmap)
        arr = []
        for key, value in hashmap.items():
            if value > 1:
                arr.append(key)
        res = 0
        for num in arr:
            res ^= num
        return res