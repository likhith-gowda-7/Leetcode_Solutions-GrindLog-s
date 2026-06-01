class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxi=max(nums)
        if(maxi<=0):
            return maxi  
        check=set()
        curr_sum=0
        res=0
        for num in nums:
            if(num<=0):
                continue
            if(num in check):
                check.remove(num)
            else:
                curr_sum+=num
            check.add(num)
            res=max(res,curr_sum)
        return res