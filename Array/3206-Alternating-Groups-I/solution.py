class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n=len(colors)
        res=0
        l=0
        for r in range(1,(n+3)-1):
            if(colors[r%n]==colors[(r-1)%n]):
                l=r
            if(r-l+1==3):
                res+=1
                l+=1  
        return res
            
        