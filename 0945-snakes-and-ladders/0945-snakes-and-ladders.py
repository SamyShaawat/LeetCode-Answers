class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        flatten=[0]*(n*n)
        for i in range(n-1, -1, -2):
            for j in range(n):
                flatten[(n-1-i)*n+j]=board[i][j]-1
                if i>=1:
                    flatten[(n-i)*n+(n-1-j)]=board[i-1][j]-1
        visited=[-1]*(n*n)
        q=deque()
        q.append(0)
        visited[0]=0
        while q:
            curr=q.popleft()
            if curr==n*n-1:
                return visited[curr]
            i0=min(6, n*n-1-curr)
            for i in range(1, i0+1):
                next=curr+i
                if flatten[next]!=-2: next=flatten[next]
                if visited[next]!=-1: continue
                visited[next]=visited[curr]+1
                q.append(next)
        return -1
        