class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left=0
        right=sum(nums)
        res=0
        for num in nums[:-1]:
            left+=num
            right-=num
            diff=abs(left-right)
            if(diff%2==0):
                res+=1
        return res