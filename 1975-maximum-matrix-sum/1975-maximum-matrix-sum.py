class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sum, minAbs=0, inf
        negOdd=False
        for row in matrix:
            for x in row:
                minAbs=min(minAbs, abs(x))
                if x<0:
                    sum-=x
                    negOdd=1-negOdd
                else:
                    sum+=x
        return sum-2*negOdd*minAbs
        