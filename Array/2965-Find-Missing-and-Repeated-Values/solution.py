class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        a=0
        h=set()
        b=(n*n)*((n*n)+1)//2
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] in h):
                    a=grid[i][j]
                else:
                    h.add(grid[i][j])
                    b-=grid[i][j]
        return a,b

