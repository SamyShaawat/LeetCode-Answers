class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        ans = []
        print(hashmap)
        for key, value in hashmap.items():
            if value == 1:
                ans.append(key)
        print(ans)
        return ans
        