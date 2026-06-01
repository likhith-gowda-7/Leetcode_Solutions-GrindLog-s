class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res=0
        curr=0
        l=0
        for r in range(len(nums)):
            while curr&nums[r]!=0:
                curr-=nums[l]
                l+=1
            curr+=nums[r]
            res=max(res,r-l+1)
        if(res==0):
            return 1
        return res
            
        