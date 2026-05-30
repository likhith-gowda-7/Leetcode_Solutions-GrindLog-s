class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        lands=0
        m=len(grid)
        n=len(grid[0])
        q=deque()
        def corner_check(row,col):
            if(row==0 or row==(m-1) or col==0 or col==(n-1)):
                return True
            return False
        for row in range(m):
            for col in range(n):
                if(grid[row][col]==1):
                    if(corner_check(row,col)):
                        q.append((row,col))
                        grid[row][col]=0
                    else:
                        lands+=1
        def check(row,col):
            if(row<0 or row>=m or col<0 or col>=n or grid[row][col]==0):
                return False
            return True 
        #Multi Source BFS
        while q:
            r,c=q.popleft()
            for row,col in [(-1,0),(1,0),(0,-1),(0,1)]:
                ro=r+row
                co=c+col
                if(check(ro,co)):
                    q.append((ro,co))
                    grid[ro][co]=0
                    lands-=1
        return lands
