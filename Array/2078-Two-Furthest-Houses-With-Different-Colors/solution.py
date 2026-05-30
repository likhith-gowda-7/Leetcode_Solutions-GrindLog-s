class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        r=len(colors)-1
        while r>0 and colors[0]==colors[r]:
            r-=1
        l=0
        while l<n and colors[-1]==colors[l]:
            l+=1
        return max(r,(n-l)-1)
