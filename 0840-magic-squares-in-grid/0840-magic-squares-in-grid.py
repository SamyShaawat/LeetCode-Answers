class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check_square(i,j, grid):

            tl = grid[i-1][j-1]
            t = grid[i-1][j]
            tr = grid[i-1][j+1]

            l = grid[i][j-1]
            mid = grid[i][j]
            r = grid[i][j+1]

            bl = grid[i+1][j-1]
            b = grid[i+1][j]
            br = grid[i+1][j+1]

            lines = [
                [tr,tl,t],
                [l,mid,r],
                [bl,mid,tr],
                [tl,mid,br],
                [tr,mid,bl],
                [tl,l,bl],
                [t,mid,b],
                [tr,r,br]
            ]

            elems = [tl,t,tr,l,mid,r,bl,b,br]
            if len(set(elems)) != 9:
                return False
            if any(not (1 <= x <= 9) for x in elems):
                return False

            return len(set(sum(x) for x in lines)) == 1

        
        res = 0
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                res += check_square(i,j,grid)
        
        return res
            