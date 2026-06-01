class Solution:
    def sumZero(self, n: int) -> List[int]:
        unique=[]
        if(n%2==1):
            unique.append(0)
            n-=1
        for i in range(1,n//2+1):
            ''' to make zero'''
            unique.append(i)
            unique.append(-i)
        return unique