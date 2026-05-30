class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m=len(grid)
        n=len(grid[0])
        res=0
        top=grid[0][0]
        if(grid[0][0]<=k):
            res+=1
        for j in range(1,n):
            grid[0][j]+=grid[0][j-1]
            if(grid[0][j]<=k):
                res+=1
        for i in range(1,m):
            grid[i][0]+=grid[i-1][0]
            if(grid[i][0]<=k):
                res+=1
        for i in range(1,m):
            for j in range(1,n):
                up=grid[i-1][j]
                left=grid[i][j-1]
                grid[i][j]+=up+left
                grid[i][j]-=grid[i-1][j-1]
                if(grid[i][j]<=k):
                    res+=1
                else:
                    break
        return res