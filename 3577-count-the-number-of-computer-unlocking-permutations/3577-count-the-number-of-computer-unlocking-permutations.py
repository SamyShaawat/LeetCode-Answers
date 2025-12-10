class Solution:
    def countPermutations(self, x: List[int]) -> int:
        return 0 if x[0]>=min(x[1:]) else factorial(len(x)-1)%(10**9+7)