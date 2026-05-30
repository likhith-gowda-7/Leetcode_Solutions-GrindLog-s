class Solution:
    def makeFancyString(self, s: str) -> str:
        c=1
        prev=s[0]
        res=s[0]
        for ch in s[1:]:
            if(ch!=prev):
                prev=ch
                c=1
            else:
                c+=1
            if(c<3):
                res+=ch
        return res