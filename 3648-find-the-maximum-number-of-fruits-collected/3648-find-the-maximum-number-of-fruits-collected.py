class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n=len(fruits)
        diag=0
        for i, row in enumerate(fruits):
            diag+=row[i]
        for i in range(n-2):
            fruits[i][n-2-i]=fruits[i][n-3-i]=0
        fruits[n-2][0]=0

        for i in range(1, n-1):
            for j in range(max(i+1, n-i-1), n-1):
                fruits[i][j]+=max(fruits[i-1][j-1], fruits[i-1][j], fruits[i-1][j+1])
            fruits[i][-1]+=max(fruits[i-1][-2], fruits[i-1][-1])
        
        for j in range(1, n-1):
            for i in range(max(j+1, n-j-1), n-1):
                fruits[i][j]+=max(fruits[i-1][j-1], fruits[i][j-1], fruits[i+1][j-1])
            fruits[-1][j]+=max(fruits[-2][j-1], fruits[-1][j-1])

        return diag+fruits[n-2][n-1]+fruits[n-1][n-2]
        