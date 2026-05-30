class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n=len(nums)
        for _ in range(n-1):
            new_arr=[]
            for i in range(1,len(nums)):
                val=(nums[i]+nums[i-1])%10
                new_arr.append(val)
            nums=new_arr
        return nums[0]