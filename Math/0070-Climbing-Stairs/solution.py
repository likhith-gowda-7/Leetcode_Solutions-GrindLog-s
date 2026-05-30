class Solution:
    def climbStairs(self, n: int) -> int:
        two_step_back,one_step_back=1,1
        for stair in range(2,n+1):
            #you can jump 1 or 2 step's from current stair
            two_step_back,one_step_back=one_step_back,one_step_back + two_step_back
        return one_step_back