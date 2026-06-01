class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        l=x
        r=(x+k)-1
        while l<r:
            for i in range(y,min(y+k,n)):
                grid[l][i],grid[r][i]=grid[r][i],grid[l][i]
            l+=1
            r-=1
        return grid