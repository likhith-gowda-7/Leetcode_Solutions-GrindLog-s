class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n=max(nums)
        dup=0
        curr=1
        if(nums[0]!=1):
            return False
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]):
                dup+=1
                if(nums[i]!=n):
                    return False
            else:
                curr+=1
        return curr==n and dup==1
        