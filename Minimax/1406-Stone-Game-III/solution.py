class Solution:
    def stoneGameIII(self, nums: List[int]) -> str:
        n=len(nums)
        @cache
        def solve(i):
            if(i>=n):
                return 0
            take1=nums[i]-solve(i+1)
            take2=float('-inf')
            if(i+1<n):
                take2=nums[i]+nums[i+1]-solve(i+2)
            take3=float('-inf')
            if(i+2<n):
                take3=nums[i]+nums[i+1]+nums[i+2]-solve(i+3)
            return max(take1,take2,take3)
        res=solve(0)
        if(res<0):
            return "Bob"
        elif(res>0):
            return "Alice"
        else:
            return "Tie"