class Solution:
    def maximizeSquareArea(self, m: int, n: int, a: List[int], b: List[int]) -> int:
        a,b = [1,*sorted(a),m],[1,*b,n]
        d = {i-j:i for i,j in product(a,b)}
        return max(d[i-j]-i for i,j in product(a,b))**2%(10**9+7) or -1