class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(any(x>y for x,y in pairwise(col)) for col in zip(*strs))