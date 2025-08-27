class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        d=(1,1,-1,-1,1) #tuple is faster
        n, m=len(grid), len(grid[0])
        def isOutSide(i, j):
            return i<0 or i>=n or j<0 or j>=m
        zero=[0]*4
        dp=[[zero[:] for _ in range(m)] for _ in range(n)]
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                if (grid[i+1][j+1]^2)==grid[i][j]:
                    dp[i][j][0]=1+dp[i+1][j+1][0]
            for j in range(1, m):
                if (grid[i+1][j-1]^2)==grid[i][j]:
                    dp[i][j][1]=1+dp[i+1][j-1][1]

        for i in range(1, n):
            for j in range(1, m):
                if (grid[i-1][j-1]^2)==grid[i][j]:
                    dp[i][j][2]=1+dp[i-1][j-1][2]
            for j in range(m-2, -1, -1):
                if (grid[i-1][j+1]^2)==grid[i][j]:
                    dp[i][j][3]=1+dp[i-1][j+1][3]
        ans=0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if grid[i][j]==1:
                    ans=max(ans, 1)
                    for dir in range(4):
                        s=i+d[dir]
                        t=j+d[dir+1]
                        if isOutSide(s, t) or grid[s][t]!=2:
                            continue
                        newDir=(dir+1)&3
                        cnt=1
                        while not isOutSide(s, t) and grid[s][t]==((cnt&1)<<1):
                            ans=max(ans,cnt+dp[s][t][newDir]+1)
                            cnt+=1
                            s+=d[dir]
                            t+=d[dir+1]
        return ans
              