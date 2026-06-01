class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        #He can't rob neighbour homes
        def is_valid(capability):
            c=0
            i=0
            while i<len(nums):
                if(nums[i]<=capability):
                    i+=2
                    c+=1
                else:
                    i+=1
                if(c==k):
                    break
            return c==k
        l=1
        r=max(nums)
        while l<=r:
            mid=l+(r-l)//2
            if(is_valid(mid)):
                r=mid-1
            else:
                l=mid+1
        return l
            

        