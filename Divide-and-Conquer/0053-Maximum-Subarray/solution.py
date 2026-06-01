class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        curr=0
        for val in nums:
            curr+=val
            curr=max(curr,val)
            ans=max(ans,curr)
        return ans