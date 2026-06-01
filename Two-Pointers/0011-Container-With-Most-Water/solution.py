class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi=0
        L=0
        R=len(height)-1
        while L<R:
            bar=min(height[L],height[R])
            length=R-L
            area=length*bar
            if(area>maxi):
                maxi=area
            if(height[L]<height[R]):
                L+=1
            else:
                R-=1
        return maxi

