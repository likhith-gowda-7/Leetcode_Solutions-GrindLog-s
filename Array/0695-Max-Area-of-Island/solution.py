class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def dfs(row,col):
            if((row<0 or row>=m) or (col<0 or col>=n)):
                return
            if(grid[row][col]==0):
                return
            nonlocal count
            count+=1
            grid[row][col]=0
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row,col+1)
        res=0
        for row in range(m):
            for col in range(n):
                if(grid[row][col]==1):
                    count=0
                    dfs(row,col)
                    res=max(res,count)
        return res