class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m=len(mat)
        n=len(mat[0])
        h1=[0]*m
        h2=[0]*n
        for i in range(m):
            for j in range(n):
                if(mat[i][j]==1):
                    h1[i]+=1
                    h2[j]+=1
        cnt=0
        for i in range(m):
            for j in range(n):
                if(mat[i][j]==1 and (h1[i]==1 and h2[j]==1)):
                    cnt+=1
        return cnt 