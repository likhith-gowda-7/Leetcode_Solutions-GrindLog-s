class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        first,second=p.split("*")
        star_idx=p.index("*")
        f1=s.find(first)
        f2=s.find(second,f1+len(first))
        return f1!=-1 and f2!=-1

