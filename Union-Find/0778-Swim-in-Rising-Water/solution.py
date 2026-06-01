class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #Modified Dijkstra
        '''The problem tells to found the path from start(0,0) to end(n-1,n-1)
        with a min_cost'''
        #min_cost-> it is the maximum number in that path
        #we'll use heap, becoz it will heap us to find the min_cost easily everytime
        #value in heap -> (min_cost,(row,col))
        n=len(grid)
        min_heap=[(grid[0][0],0,0)]
        #for marking a node visited, we'll do it in-place. (-1) in grid...
        def check(row,col):
            if(row<0 or row==n or col<0 or col==n or grid[row][col]==-1):
                return False
            return True
        while min_heap:
            path_max,Row,Col=heappop(min_heap)
            if((Row,Col)==(n-1,n-1)):
                return path_max
            for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
                ro=Row+r
                co=Col+c
                if(check(ro,co)):
                    curr_max=max(grid[ro][co],path_max)
                    heappush(min_heap,(curr_max,ro,co))
                    #mark it as visited
                    grid[ro][co]=-1
        