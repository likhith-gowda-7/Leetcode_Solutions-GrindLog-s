class Solution:
    def jump(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return 0
        l=1
        r=nums[0]
        res=1
        while r<len(nums)-1:
            highest=0
            for i in range(l,r+1):
                highest=max(highest,nums[i]+i)
            l=r+1
            r=highest
            res+=1
        return res

        