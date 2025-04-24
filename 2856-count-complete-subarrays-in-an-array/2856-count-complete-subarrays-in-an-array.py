class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_elements = set(nums)
        total_distinct = len(distinct_elements)
        count = 0
        n = len(nums)
        
        for i in range(n):
            current_set = set()
            for j in range(i, n):
                current_set.add(nums[j])
                if len(current_set) == total_distinct:
                    count += (n - j)
                    break
        return count