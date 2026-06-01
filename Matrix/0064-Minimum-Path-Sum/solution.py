class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #Tabulation(Bottom-up)
        m=len(grid)
        n=len(grid[0])
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=grid[0][0]
        for row in range(1,m):
            dp[row][0]=grid[row][0]+dp[row-1][0]
        for col in range(1,n):
            dp[0][col]=grid[0][col]+dp[0][col-1]
        for i in range(1,m):
            for j in range(1,n):
                up=dp[i-1][j]
                left=dp[i][j-1]
                path_sum=grid[i][j]+min(up,left)
                dp[i][j]=path_sum
        return dp[m-1][n-1]