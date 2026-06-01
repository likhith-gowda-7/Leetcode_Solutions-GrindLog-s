class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        mini=nums[0]
        while l<=r:
            while l<r and nums[l]==nums[l+1]:
                l+=1
            while l<r and nums[r]==nums[r-1]:
                r-=1
            mid=(l+r)//2
            if(nums[l]<=nums[mid]):
                mini=min(mini,nums[l])
                l=mid+1
            else:
                mini=min(mini,nums[mid])
                r=mid-1
        return mini