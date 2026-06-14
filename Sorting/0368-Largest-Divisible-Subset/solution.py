class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums.sort()
        div_set=list(range(n))
        dp=[1]*n
        max_len=1
        last_idx=0
        for i in range(1,n):
            for prev in range(i):
                if(nums[i]%nums[prev]==0 and dp[prev]+1>dp[i]):
                    div_set[i]=prev
                    dp[i]=dp[prev]+1
            if(dp[i]>max_len):
                max_len=dp[i]
                last_idx=i
        res=[]
        while last_idx!=div_set[last_idx]:
            res.append(nums[last_idx])
            last_idx=div_set[last_idx]
        res.append(nums[last_idx])
        return res


