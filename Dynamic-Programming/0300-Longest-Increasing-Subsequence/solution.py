class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        ans=[nums[0]]
        res=1
        for i in range(1,n):
            l=0
            r=res
            while l<r:
                mid=(l+r)//2
                if(ans[mid]>=nums[i]):
                    r=mid
                else:
                    l=mid+1
            if(l>=res):
                ans.append(nums[i])
                res+=1
            else:
                ans[l]=nums[i]
        return res