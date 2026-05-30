class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        #Bottom-Up(tab)
        n=len(matrix)
        def check(r,c):
            if(r<0 or r==n or c<0 or c==n):
                return float('inf')
            else:
                return matrix[r][c]
        for row in range(n-2,-1,-1):
            for col in range(n):
                '''Three Options:
                    1.Down -> check(row+1,col)
                    2.Left -> check(row+1,col-1)
                    3.Right -> check(row+1,col+1)
                    '''
                matrix[row][col]+=min(check(row+1,col),check(row+1,col-1),check(row+1,col+1))
        return min(matrix[0])