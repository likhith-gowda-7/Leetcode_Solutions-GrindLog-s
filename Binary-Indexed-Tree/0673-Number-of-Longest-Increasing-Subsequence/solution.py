class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        counts=[1]*n
        maxi=1
        for i in range(1,n):
            for prev in range(i):
                if(nums[prev]<nums[i] and (dp[prev]+1)>dp[i]):
                    dp[i]=dp[prev]+1
                    counts[i]=counts[prev]
                elif(nums[prev]<nums[i] and (dp[prev]+1)==dp[i]):
                    counts[i]+=counts[prev]
            if(dp[i]>maxi):
                maxi=dp[i]
        no_of_lis=0
        for i in range(n):
            if(dp[i]==maxi):
                no_of_lis+=counts[i]
        return no_of_lis
        