class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res=[]
        total=sum(nums)
        left=0
        for i in range(len(nums)):
            right=total-left-nums[i]
            val=abs(right-left)
            res.append(val)
            left+=nums[i]
        return res


        