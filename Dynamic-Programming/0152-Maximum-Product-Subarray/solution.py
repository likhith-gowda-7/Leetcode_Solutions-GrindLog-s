class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        mini=nums[0]
        maxi=nums[0]
        for val in nums[1:]:
            if(val==0):
                maxi=1
                mini=1
            else:
                temp=max(val,maxi*val,mini*val)
                mini=min(val,maxi*val,mini*val)
                maxi=temp
                res=max(res,maxi)
        return res