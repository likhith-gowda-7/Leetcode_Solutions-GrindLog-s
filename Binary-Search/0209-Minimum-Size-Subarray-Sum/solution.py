class Solution(object):
    def minSubArrayLen(self, target, nums):
        res=float('inf')
        l=0
        curr=0
        for r in range(len(nums)):
            curr+=nums[r]
            while curr>=target:
                res=min(res,r-l+1)
                curr-=nums[l]
                l+=1
        if(res==float('inf')):
            res=0
        return res