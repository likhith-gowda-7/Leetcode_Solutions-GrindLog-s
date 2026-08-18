class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        h1=Counter(nums)
        if(k==n):
            return max(nums)
        if(k==1):
            res=-1
            for key,val in h1.items():
                if(val==1):
                    res=max(res,key)
            return res
        if(h1[nums[0]]>1 and h1[nums[-1]]>1):
            return -1
        res=nums[0] if(h1[nums[0]]==1) else 0
        if(nums[-1]>res and h1[nums[-1]]==1):
            res=nums[-1]
        return res