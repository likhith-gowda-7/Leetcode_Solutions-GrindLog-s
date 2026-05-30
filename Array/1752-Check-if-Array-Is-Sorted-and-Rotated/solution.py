class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        streak=0
        for i in range(1,n*2):
            i%=n
            prev=nums[i-1]
            curr=nums[i]
            if(prev<=curr):
                streak+=1
                if(streak==n):
                    return True
            else:
                streak=1
        return False