class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix),len(matrix[0])
        spiral_directions=[(0,1),(1,0),(0,-1),(-1,0)]
        res=[]
        curr_dir=0
        def dfs(i,j):
            nonlocal curr_dir
            res.append(matrix[i][j])
            matrix[i][j]="#"
            curr_i=i+spiral_directions[curr_dir][0]
            curr_j=j+spiral_directions[curr_dir][1]
            if(curr_i<0 or curr_j<0 or curr_i>=m or curr_j>=n or matrix[curr_i][curr_j]=="#"):
                curr_dir+=1
                curr_dir%=4
            curr_i=i+spiral_directions[curr_dir][0]
            curr_j=j+spiral_directions[curr_dir][1]
            if((0<=curr_i<m and 0<=curr_j<n) and matrix[curr_i][curr_j]!="#"):
                dfs(curr_i,curr_j)
        dfs(0,0)
        return res