class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m=len(grid)
        n=len(grid[0])
        @cache
        def dfs(row,col,validity):
            if(row>=m or col>=n or validity<0):
                return False
            curr=validity
            if(grid[row][col]=="("):
                curr+=1
            else:
                curr-=1
            if((row,col)==(m-1,n-1) and curr==0):
                return True
            down=dfs(row+1,col,curr)
            right=dfs(row,col+1,curr)
            return (down or right)
        return dfs(0,0,0)