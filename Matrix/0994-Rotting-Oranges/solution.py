class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Multi Source BFS Solution
        m=len(grid)
        n=len(grid[0])
        q=deque()
        ones=0
        #append all rotten oranges to queue
        for row in range(m):
            for col in range(n):
                if(grid[row][col]==2):
                    q.append((row,col))
                    grid[row][col]=0
                elif(grid[row][col]):
                    ones+=1
        def add_item(row,col):
            if((row<0 or row>=m) or (col<0 or col>=n) or grid[row][col]==0):
                return 
            q.append((row,col))
            grid[row][col]=0
            nonlocal ones
            ones-=1
        min_time=0
        while q:
            #Multi Source BFS
            for _ in range(len(q)):
                r,c=q.popleft()
                add_item(r-1,c)
                add_item(r+1,c)
                add_item(r,c-1)
                add_item(r,c+1)
            min_time+=1
        if(min_time>0):
            min_time-=1
        return min_time if(not ones) else -1
                