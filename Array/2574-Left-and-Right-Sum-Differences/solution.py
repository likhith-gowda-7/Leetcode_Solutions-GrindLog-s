class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right_sum=sum(nums)
        left_sum=0
        ans=[]
        for val in nums:
            right_sum-=val
            ans.append(abs(left_sum-right_sum))
            left_sum+=val
        return ans