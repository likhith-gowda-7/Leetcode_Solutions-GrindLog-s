class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        q=deque()
        for row in range(n-1,-1,-1):
            q.append((row,0))
        for col in range(1,n):
            q.append((0,col))
        def get_diagonals(row,col,ele):
            while (0<=row<n) and (0<=col<n):
                ele.append(grid[row][col])
                #go in its diagonal
                row+=1
                col+=1
        def write_diagonals(row,col,ele):
            idx=0
            while (0<=row<n) and (0<=col<n):
                #here we change the value with the sorted value
                grid[row][col]=ele[idx]
                idx+=1
                #go in its diagonal
                row+=1
                col+=1
        #this variable tells that the order of elements should be in increasing or decreasing
        rev=True
        while q:
            row,col=q.popleft()
            ele=[]
            #this function gets all the same diagonals values
            get_diagonals(row,col,ele)
            ele.sort(reverse=rev)
            #this function changes values with the sorted value in daigonals
            write_diagonals(row,col,ele)
            if((row,col)==(0,0)):
                rev=False
        return grid

