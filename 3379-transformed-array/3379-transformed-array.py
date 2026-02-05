class Solution:
    def constructTransformedArray(self, A: List[int]) -> List[int]:
        return [A[(i + v) % len(A)] for i, v in enumerate(A)]
