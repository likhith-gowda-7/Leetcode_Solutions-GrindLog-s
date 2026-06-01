class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid=[[0]*n for _ in range(m)]
        """states of grid
        0 -> unguarded
        1 -> wall
        2 -> guard
        3 -> guard watching
        """
        unguarded=m*n
        #prefilling walls
        for row,col in walls:
            grid[row][col]=1
            unguarded-=1
        for row,col in guards:
            grid[row][col]=2
            unguarded-=1
        def guards_vision(row,col):
            nonlocal unguarded
            #for UP
            for r in reversed(range(0,row)):
                if(grid[r][col] in [1,2]):
                    break
                if(grid[r][col]==0):
                    grid[r][col]=3
                    unguarded-=1
            #for down
            for r in range(row+1,m):
                if(grid[r][col] in [1,2]):
                    break
                if(grid[r][col]==0):
                    grid[r][col]=3
                    unguarded-=1
            #for left
            for c in reversed(range(0,col)):
                if(grid[row][c] in [1,2]):
                    break
                if(grid[row][c]==0):
                    grid[row][c]=3
                    unguarded-=1
            #for right
            for c in range(col+1,n):
                if(grid[row][c] in [1,2]):
                    break
                if(grid[row][c]==0):
                    grid[row][c]=3
                    unguarded-=1
        for r,c in guards:
            guards_vision(r,c)
        return unguarded