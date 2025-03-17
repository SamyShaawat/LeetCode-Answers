class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        dicty = defaultdict(int)
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] == key:
                dicty[nums[i]]+=1
        print(dicty)
        maxcount = max(dicty.values())
        for key in dicty:
            if dicty[key] == maxcount:
                return key



        