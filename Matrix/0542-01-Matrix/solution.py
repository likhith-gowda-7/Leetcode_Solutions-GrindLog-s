class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        q=deque()
        visited=[[1]*n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                if(mat[row][col]==0):
                    q.append((row,col))
                    visited[row][col]=0
        def check(row,col,dist):
            if(row<0 or row>=m or col<0 or col>=n or visited[row][col]==0):
                return
            q.append((row,col))
            #mark it as visited
            visited[row][col]=0
            mat[row][col]=dist
        dist=1
        while q:
            for _ in range(len(q)):
                row,col=q.popleft()
                check(row-1,col,dist)
                check(row+1,col,dist)
                check(row,col-1,dist)
                check(row,col+1,dist)
            dist+=1
        return mat
            

