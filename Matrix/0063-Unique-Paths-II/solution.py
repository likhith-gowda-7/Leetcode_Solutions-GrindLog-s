class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        #Top-Down DP
        #edge case, if the goal itself is an abstacle then you can't reach it in any way
        m,n=len(grid),len(grid[0])
        if(grid[m-1][n-1]==1):
            return 0
        #Setting up base cases
        memo={(m-1,n-1):1}
        def dfs(row,col):
            if(row>=m or col>=n or grid[row][col]==1):
                return 0
            if((row,col) not in memo):
                memo[(row,col)]=dfs(row+1,col)+dfs(row,col+1)
            return memo[(row,col)]
        return dfs(0,0)