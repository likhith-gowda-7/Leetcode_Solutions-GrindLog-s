class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        length=len(nums)
        def check(mid,length):
            pairs=0
            i=1
            while i<length:
                diff=nums[i]-nums[i-1]
                if(diff<=mid):
                    pairs+=1
                    i+=2
                else:
                    i+=1
            return pairs>=p
        
        left=0
        right=nums[-1]-nums[0]
        while left<=right:
            mid=(left+right)//2
            if(check(mid,length)):
                right=mid-1
            else:
                left=mid+1
        return left




        