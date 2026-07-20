class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        k%=(m*n)
        if(k==0):
            return grid
        last=(m*n)
        dummy=[0]*last
        for row in range(m):
            for col in range(n):
                idx=(row*n)+col
                new_idx=(idx+k)%last
                dummy[new_idx]=grid[row][col]
        for i in range(last):
            grid[i//n][i%n]=dummy[i]
        return grid