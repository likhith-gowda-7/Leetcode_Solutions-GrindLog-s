class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m=len(grid)
        n=len(grid[0])
        if(grid[0][0]>health):
            return False
        heap=[(-health,0,0)]
        seen=set()
        while heap:
            life,row,col=heappop(heap)
            life*=-1
            diff=life-grid[row][col]
            if(diff<1 or (row,col) in seen):
                continue
            if((row,col)==(m-1,n-1)):
                return True
            seen.add((row,col))
            for r,c in [(-1,0),(1,0),(0,-1),(0,1)]:
                ro=row+r
                co=col+c
                if(0<=ro<m and 0<=co<n and (ro,co) not in seen):
                    heappush(heap,(-diff,ro,co))
        return False
            