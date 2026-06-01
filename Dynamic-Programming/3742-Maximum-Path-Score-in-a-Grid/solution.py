class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[-1]*(k+1) for _ in range(n+1)]
        for i in range(m-1,-1,-1):
            curr=[[-1]*(k+1) for _ in range(n+1)]
            for j in range(n-1,-1,-1):
                for cost in range(k,-1,-1):
                    val=grid[i][j]
                    diff=cost+(val>0)
                    if((i,j)==(m-1,n-1)):
                        if(diff<=k):
                            curr[j][cost]=grid[i][j]
                        continue
                    if(diff<=k):
                        down = dp[j][diff] if i < m-1 else -1
                        right = curr[j+1][diff] if j < n-1 else -1
                        maxi = max(down, right)
                        if(maxi!=-1):
                            curr[j][cost]=val+maxi
            dp=curr
        return dp[0][0]
