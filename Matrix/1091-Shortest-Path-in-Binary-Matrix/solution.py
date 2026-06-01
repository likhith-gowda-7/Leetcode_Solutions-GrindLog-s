class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if(grid[0][0]==1 or grid[n-1][n-1]==1):
            return -1
        #Invert Thinking(start from destination and trying to reach source)
        target=(0,0)
        def check(row,col):
            if(row<0 or row>=n or col<0 or col>=n or grid[row][col]==1):
                return False
            return True
        #row,col,distance
        q=deque()
        #we'll start from distination
        q.append((n-1,n-1,1))
        #mark it as visited
        grid[n-1][n-1]=1
        #all 8-directions
        directions=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        while q:
            row,col,dist=q.popleft()
            if((row,col)==target):
                return dist
            for r,c in directions:
                ro=row+r
                co=col+c
                if(check(ro,co)):
                    grid[ro][co]=1
                    q.append((ro,co,dist+1))
        return -1