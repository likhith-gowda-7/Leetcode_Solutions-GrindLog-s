class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(not nums):
            return [-1,-1]
        l=0
        r=len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if(nums[mid]>target):
                r=mid-1
            else:
                l=mid+1
        right=r
        if(nums[r]!=target):
            right=-1
        l=0
        r=len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if(nums[mid]>=target):
                r=mid-1
            else:
                l=mid+1
        left=l
        if(l==len(nums) or nums[l]!=target):
            left=-1
        return [left,right]
        


                                    