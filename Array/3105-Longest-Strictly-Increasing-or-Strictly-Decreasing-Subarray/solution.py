class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if(len(nums)<2):
            return 1
        maxi=1
        count=1
        for i in range(1,len(nums)):
            if(nums[i]>nums[i-1]):
                count+=1
                maxi=max(count,maxi)
            else:
                count=1
        count=1
        for i in range(1,len(nums)):
            if(nums[i]<nums[i-1]):
                count+=1
                maxi=max(count,maxi)
            else:
                count=1
        return maxi