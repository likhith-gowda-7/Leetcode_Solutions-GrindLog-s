class Solution:
    def stoneGameIII(self, nums: List[int]) -> str:
        n=len(nums)
        take1=take2=take3=0
        for i in range(n-1,-1,-1):
            res=nums[i]-take1
            if(i+2<=n):
                res=max(res,nums[i]+nums[i+1]-take2)
            if(i+3<=n):
                res=max(res,nums[i]+nums[i+1]+nums[i+2]-take3)
            #State Saving
            take3=take2
            take1,take2=res,take1
        ans=take1
        if(ans<0):
            return "Bob"
        elif(ans>0):
            return "Alice"
        else:
            return "Tie"


