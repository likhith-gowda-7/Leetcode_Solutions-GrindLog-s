class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n=len(s)
        num=[int(c) for c in s]
        while n>2:
            curr=[]
            for i in range(1,n):
                op=(num[i-1]+num[i])%10
                curr.append(op)
            num=curr
            n-=1
        return num[0]==num[1]