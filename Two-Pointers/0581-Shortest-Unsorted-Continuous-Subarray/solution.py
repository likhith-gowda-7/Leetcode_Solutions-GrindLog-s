class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n1=sorted(nums)
        if(nums==n1 or len(nums)==1):
            return 0
        l,r=0,len(nums)-1
        while l<r:
            if(nums[l]==n1[l]):
                l+=1
            if(nums[r]==n1[r]):
                r-=1
            if(nums[l]!=n1[l] and nums[r]!=n1[r]):
                break
        return r-l+1
