class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        res = []
        n = len(nums)
        for key, value in hashmap.items():
           if value > math.floor(n/2) :
                res.append(key)
        return max(res)
        
