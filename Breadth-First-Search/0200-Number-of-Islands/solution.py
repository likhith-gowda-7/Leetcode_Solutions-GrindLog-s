class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def dfs(row,col):
            if((row<0 or row>=m) or (col<0 or col>=n)):
                return
            if(grid[row][col]=="0"):
                return
            #changing the visited value from land to water, to avoid revisited
            grid[row][col]="0"
            #up
            dfs(row-1,col)
            #down
            dfs(row+1,col)
            #left
            dfs(row,col-1)
            #right
            dfs(row,col+1)
        islands_count=0
        for i in range(m):
            for j in range(n):
                if(grid[i][j]=="1"):
                    dfs(i,j)
                    islands_count+=1
        return islands_count

            