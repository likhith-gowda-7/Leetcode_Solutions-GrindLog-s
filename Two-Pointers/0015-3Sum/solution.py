class Solution(object):
    def threeSum(self, nums):
        res=[]
        nums.sort()
        for i,val in enumerate(nums):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                ts=val+nums[l]+nums[r]
                if(ts>0):
                    r-=1
                elif(ts<0):
                    l+=1
                else:
                    li=[val,nums[l],nums[r]]
                    res.append(li)
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res
            

        