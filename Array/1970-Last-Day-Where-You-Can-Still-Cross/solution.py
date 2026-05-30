class Solution:
    def latestDayToCross(self, rows: int, cols: int, cells: List[List[int]]) -> int:
        for i in range(len(cells)):
            cells[i][0]-=1
            cells[i][1]-=1
        def find(mid):
            mat=[[0]*cols for _ in range(rows)]
            for i in range(mid+1):
                r,c=cells[i]
                mat[r][c]=1
            q=deque()
            for i in range(cols):
                if(mat[0][i]==0):
                    q.append((0,i))
                    mat[0][i]=1
            while q:
                row,col=q.popleft()
                if(row==(rows-1)):
                    return True
                for r,c in [(-1,0),(1,0),(0,-1),(0,1)]:
                    curr_row=row+r
                    curr_col=col+c
                    if(curr_row<0 or curr_row>=rows or curr_col<0 or curr_col>=cols or mat[curr_row][curr_col]==1):
                        continue
                    q.append((curr_row,curr_col))
                    mat[curr_row][curr_col]=1
            return False

        l=0
        r=len(cells)-1
        while l<=r:
            mid=(l+r)//2
            if(find(mid)):
                l=mid+1
            else:
                r=mid-1
        return l
                