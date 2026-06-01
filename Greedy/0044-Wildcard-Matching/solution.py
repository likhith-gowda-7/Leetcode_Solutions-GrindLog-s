class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1=len(s)
        n2=len(p)
        i=0
        j=0
        star=-1
        matched=0
        while i<n1:
            if(j<n2 and (s[i]==p[j] or p[j]=="?")):
                i+=1
                j+=1
            elif(j<n2 and p[j]=="*"):
                star=j
                matched=i
                j+=1
            elif(star!=-1):
                j=star+1
                matched+=1
                i=matched
            else:
                return False
        while j<n2 and p[j]=="*":
            j+=1
        return j==n2