class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        sol=[["." for _ in range(n)] for i in range(n)]
        pos_dia=[False]*(n*n)
        neg_dia=[False]*(n*n)
        used_col=[False]*n
        def backtrack(row,sol):
            if(row==n):
                val=[]
                for i in range(n):
                    val.append("".join(sol[i]))
                res.append(val)
                return
            for col in range(n):
                d1=row+col    #for positive diagonal
                d2=row-col    #for negative diagonal
                if(not used_col[col] and (not pos_dia[d1] and not neg_dia[d2])):
                    pos_dia[d1]=True
                    neg_dia[d2]=True
                    used_col[col]=True
                    sol[row][col]="Q"
                    backtrack(row+1,sol)
                    sol[row][col]="."
                    used_col[col]=False
                    pos_dia[d1]=False
                    neg_dia[d2]=False
        backtrack(0,sol)
        return res
        
