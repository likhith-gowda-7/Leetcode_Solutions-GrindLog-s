class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        res=[]
        def check(row,col):
            if(row<0 or row>=m or col<0 or col>=n):
                return False
            return True
        for d in range(m+n-1):
            diag=[]
            r=0 if(d<n) else d-n+1
            c=d if(d<n) else n-1
            while check(r,c):
                diag.append(mat[r][c])
                r+=1
                c-=1
            #concate the lists
            if(d%2==0):
                res.extend(diag[::-1])
            else:
                res.extend(diag)
        return res

        

        