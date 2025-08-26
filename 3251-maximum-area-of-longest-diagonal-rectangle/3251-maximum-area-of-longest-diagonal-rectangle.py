class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = -1 
        res = 0
        for l,w in dimensions:
            diagonal = sqrt(l*l + w*w)
            if diagonal > max_diagonal:
                max_diagonal = diagonal
                res = l * w
            elif diagonal == max_diagonal:
                res = max(res, l*w)

        return res
        

                        
        