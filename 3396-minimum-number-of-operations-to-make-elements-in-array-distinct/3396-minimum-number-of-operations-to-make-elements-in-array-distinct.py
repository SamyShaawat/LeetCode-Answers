class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def is_unique(start):
            seen = set()
            for num in nums[start:]:
                if num in seen:
                    return False
                seen.add(num)
            return True

        ops = 0
        for i in range(0, len(nums), 3):
            if is_unique(i):
                return ops
            ops +=1

        return ops
        