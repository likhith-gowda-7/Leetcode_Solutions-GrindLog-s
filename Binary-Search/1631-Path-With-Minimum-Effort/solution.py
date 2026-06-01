class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #Dijsktra based solution with Invert thinking
        m=len(heights)
        n=len(heights[0])
        efforts_mat=[[float("inf")]*n for _ in range(m)]
        heap=[(0,m-1,n-1)]
        #premark the starting point effort
        efforts_mat[m-1][n-1]=0
        def check(row,col):
            if(row<0 or row>=m or col<0 or col>=n):
                return False
            return True
        while heap:
            effort,row,col=heappop(heap)
            if((row,col)==(0,0)):
                return effort
            for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
                ro=row+r
                co=col+c
                if(check(ro,co)):
                    diff=abs(heights[row][col]-heights[ro][co])
                    ef=max(effort,diff)
                    if(ef<efforts_mat[ro][co]):
                        heappush(heap,(ef,ro,co))
                        efforts_mat[ro][co]=ef
        return -1


        