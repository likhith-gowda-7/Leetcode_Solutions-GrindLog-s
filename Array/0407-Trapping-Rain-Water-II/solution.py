class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows=len(heightMap)
        cols=len(heightMap[0])
        min_heap=[]
        #Step=1
        #Add all border
        for row in range(rows):
            #adding the left border
            min_heap.append((heightMap[row][0],row,0))
            #adding the right border
            min_heap.append((heightMap[row][cols-1],row,cols-1))
            #marking them visited
            heightMap[row][0]=-1
            heightMap[row][cols-1]=-1
        for col in range(1,cols-1):
             #adding the Top border
            min_heap.append((heightMap[0][col],0,col))
            #adding the Bottom border
            min_heap.append((heightMap[rows-1][col],rows-1,col))
            #marking them visited
            heightMap[0][col]=-1
            heightMap[rows-1][col]=-1
        heapify(min_heap)
        def check(row,col):
            if(row<0 or row>=rows or col<0 or col>=cols or heightMap[row][col]==-1):
                return False
            return True
        #Step=2
        #remove the minimum heighted building
        max_h=0
        res=0
        while min_heap:
            h,Row,Col=heappop(min_heap)
            max_h=max(max_h,h)
            res+=max_h-h
            #check it's all four directions(up,down,left,right)
            for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
                ro=Row+r
                co=Col+c
                if(check(ro,co)):
                    #add to the heap
                    heappush(min_heap,(heightMap[ro][co],ro,co))
                    #mark it as visited
                    heightMap[ro][co]=-1
        return res

