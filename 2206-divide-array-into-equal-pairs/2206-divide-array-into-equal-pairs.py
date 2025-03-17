class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashmap = Counter(nums)
        print(hashmap)
        for key, value in hashmap.items():
            if value % 2:
                return False
            else:
                continue
        return True