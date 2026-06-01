class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        total=nums[0]
        mini1=float('inf')
        mini2=float('inf')
        for n in nums[1:]:
            if(n<mini1):
                mini2=mini1
                mini1=n
            elif(n<mini2):
                mini2=n
        total+=mini1+mini2
        return total

