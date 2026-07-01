class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if(grid[0][0]==1 or grid[n-1][n-1]):
            return 0
        seen=set()
        thiefs=deque()
        for row in range(n):
            for col in range(n):
                if(grid[row][col]==1):
                    thiefs.append((row,col))
                    grid[row][col]=0
                    seen.add((row,col))
        while thiefs:
            row,col=thiefs.popleft()
            for r,c in [(-1,0),(1,0),(0,-1),(0,1)]:
                ro=row+r
                co=col+c
                if(0<=ro<n and 0<=co<n):
                    if((ro,co) not in seen):
                        thiefs.append((ro,co))
                        grid[ro][co]=1+grid[row][col]
                        seen.add((ro,co))
        heap=[(-grid[0][0],0,0)]
        seen.clear()
        seen.add((0,0))
        safe_factor=grid[0][0]
        while heap:
            distance,row,col=heappop(heap)
            safe_factor=min(safe_factor,-distance)
            if((row,col)==(n-1,n-1)):
                return safe_factor
            for r,c in [(-1,0),(1,0),(0,-1),(0,1)]:
                ro=row+r
                co=col+c
                if(0<=ro<n and 0<=co<n):
                    if((ro,co) not in seen):
                        heappush(heap,(-grid[ro][co],ro,co))
                        seen.add((ro,co))
            
        
        