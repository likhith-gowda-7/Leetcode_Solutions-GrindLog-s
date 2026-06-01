class Solution:
    def minimumAbsDifference(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        min_diff=float('inf')
        res=[]
        for i in range(1,n):
            curr_diff=nums[i]-nums[i-1]
            if(curr_diff<min_diff):
                min_diff=curr_diff
        for i in range(1,n):
            curr_diff=nums[i]-nums[i-1]
            if(curr_diff==min_diff):
                res.append([nums[i-1],nums[i]])
        return res