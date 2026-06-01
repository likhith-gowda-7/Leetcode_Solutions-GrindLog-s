class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        total=sum(nums)
        if(target>total or (total-target)%2):
            return 0
        target=(total-target)//2
        dp=[0]*(target+1)
        dp[0]=1
        for num in nums:
            for s in range(target,num-1,-1):
                dp[s]+=dp[s-num]
        return dp[target]