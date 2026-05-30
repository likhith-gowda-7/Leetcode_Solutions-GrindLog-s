class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        curr=0
        res=[]
        for sp in spaces:
            res.append(s[curr:sp])
            res.append(" ")
            curr=sp
        res.append(s[curr:])
        return "".join(res)            
        