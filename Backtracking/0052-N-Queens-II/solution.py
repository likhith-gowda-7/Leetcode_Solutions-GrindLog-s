class Solution:
    def totalNQueens(self, n: int) -> int:
        count=0
        #Boolean array to keep track of attacking diagonals and already used columns
        diagonal=[False]*(n*2)
        anti_diagonal=[False]*(n*2)
        used_col=[False]*n
        def backtracking(row):
            if(row==n):
                nonlocal count
                count+=1
                return
            #checking each columns and find the valid one
            for col in range(n):
                #trick to track the diagonals
                d1=row+col
                d2=row-col
            #this check whether the column is used or not and whether this spot is attacked by other queens??, if so then skip this spot!!!
                if((not used_col[col]) and (not diagonal[d1] and not anti_diagonal[d2])):
                    used_col[col]=True
                    diagonal[d1]=True
                    anti_diagonal[d2]=True
                    #going for next queen to be placed
                    backtracking(row+1)
                    #undo the changes
                    used_col[col]=False
                    diagonal[d1]=False
                    anti_diagonal[d2]=False
        backtracking(0)
        return count