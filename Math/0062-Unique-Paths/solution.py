class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #Bottom-UP DP
        "Space Optimized"
        dp=[]
        for row in range(m):
            dp.append([])
            for col in range(n):
                if(row==0 or col==0):
                    dp[row].append(1)
                else:
                    dp[row].append(dp[row-1][col] + dp[row][col-1])
        return dp[m-1][n-1]

