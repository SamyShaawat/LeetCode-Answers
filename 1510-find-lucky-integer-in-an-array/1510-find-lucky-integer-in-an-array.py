class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max([key if key == value else -1 for key, value in Counter(arr).items()])