class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        res=0
        zero_count=0
        for r in range(n):
            if(nums[r]==0):
                zero_count+=1
            if(zero_count>1):
                res=max(res,(r-l)-1)
                while zero_count>1:
                    if(nums[l]==0):
                        zero_count-=1
                    l+=1
        res=max(res,(n-l)-1)
        return res
