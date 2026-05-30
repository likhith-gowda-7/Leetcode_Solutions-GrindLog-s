class Solution:
    def customSortString(self, order: str, s: str) -> str:
        h1={}
        for i in range(len(order)):
            h1[order[i]]=i
        s=sorted(s,key=lambda x:h1.get(x,26))
        return "".join(s)
        
