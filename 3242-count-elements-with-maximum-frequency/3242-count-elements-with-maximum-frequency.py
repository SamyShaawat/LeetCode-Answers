class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        h = Counter(nums)
        max_value = 0 
        appearence = 0
        for key, value in h.items():
            max_value = max(max_value, value)
        for value in h.values():
            if value == max_value: 
                appearence +=1 
        return appearence * max_value
            