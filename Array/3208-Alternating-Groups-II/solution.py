class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        res=0
        l=0
        for i in range(k-1):
            colors.append(colors[i])
        n=len(colors)
        for r in range(1,n):
            if(colors[r]==colors[r-1]):
                l=r
            if(r-l+1==k):
                l+=1
                res+=1
        return res
        
        
        