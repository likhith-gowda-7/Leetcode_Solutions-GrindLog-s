class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        left_max=0
        right_max=0
        res=0
        while left<right:
            if(height[right]>height[left]):
                left_max=max(left_max,height[left])
                res+=(left_max-height[left])
                left+=1
            else:
                right_max=max(right_max,height[right])
                res+=(right_max-height[right])
                right-=1
        return res