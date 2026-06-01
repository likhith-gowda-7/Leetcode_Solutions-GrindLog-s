class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if(len(nums)==1):
            return True
        i=0
        goal=len(nums)-1
        for i in range(goal-1,-1,-1):
            if(i+nums[i]>=goal):
                goal=i
        return goal==0

        