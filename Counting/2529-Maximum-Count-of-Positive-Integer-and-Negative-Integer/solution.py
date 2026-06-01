class Solution(object):
    def maximumCount(self, nums):
        def pos(nums):
            l=0
            r=len(nums)-1
            while l<=r:
                mid=l+(r-l)//2
                if(nums[mid]<=0):
                    l=mid+1
                else:
                    r=mid-1
            return l
        def neg(nums):
            l=0
            r=len(nums)-1
            while l<=r:
                mid=l+(r-l)//2
                if(nums[mid]>=0):
                    r=mid-1
                else:
                    l=mid+1
            return l
        pos=pos(nums)
        neg=neg(nums)
        return max(len(nums[:neg]),len(nums[pos:]))