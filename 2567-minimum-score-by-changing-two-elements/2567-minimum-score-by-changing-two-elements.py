class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        a, b, c = nsmallest(3, nums)
        x, y, z = nlargest(3, nums)
        return min(x - c, z - a, y - b)
