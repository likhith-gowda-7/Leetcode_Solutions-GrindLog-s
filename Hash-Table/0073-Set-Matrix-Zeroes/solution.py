class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_zeros=set()
        col_zeros=set()
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]==0):
                    row_zeros.add(i)
                    col_zeros.add(j)
        for i in range(m):
            for j in range(n):
                if(i in row_zeros or j in col_zeros):
                    matrix[i][j]=0
        