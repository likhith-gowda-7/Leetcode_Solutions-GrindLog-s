class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        part=[]
        n=len(s)
        def palin(l,r):
            while l<r:
                if(s[l]!=s[r]):
                    return False
                l+=1
                r-=1
            return True
        def backtrack(start):
            if(start==n):
                res.append(part.copy())
                return
            #check for every subset
            for i in range(start,n):
                #check if its palindrome
                if(palin(start,i)):
                    part.append(s[start:i+1])
                    backtrack(i+1)
                    part.pop()
        backtrack(0)
        return res
                    