class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        stepsx = abs(z-x)
        print(stepsx)
        stepsy = abs(z-y)
        print(stepsy)
        if stepsx < stepsy:
            return 1
        elif stepsx > stepsy:
            return 2
        else:
            return 0
        
        