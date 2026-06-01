class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        up=None
        down=None
        for r in range(m):
            for c in range(n):
                #for up
                if(grid[r][c]==1 and up==None):
                    up=r
                #for down
                d=m-(r+1)
                if(grid[d][c]==1 and down==None):
                    down=d
                #early exit after finding
                if(up!=None and down!=None):
                    break
        left=None
        right=None
        for c in range(n):
            for r in range(m):
                #for left
                if(grid[r][c]==1 and left==None):
                    left=c
                #for right side
                rs=n-(c+1)
                if(grid[r][rs]==1 and right==None):
                    right=rs
                #early exit after finding
                if(left!=None and right!=None):
                    break
        height=(down-up)+1
        width=(right-left)+1
        return height*width
