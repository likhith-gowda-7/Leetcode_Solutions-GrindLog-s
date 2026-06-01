class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remain=sum(nums)%p
        if(remain==0):
            return 0
        res=len(nums)
        curr_sum=0
        prefix_map={0:-1}
        for i,num in enumerate(nums):
            curr_sum=(curr_sum + num)%p
            prefix=(curr_sum-remain + p)%p
            if(prefix in prefix_map):
                length=i-prefix_map[prefix]
                res=min(res,length)
            prefix_map[curr_sum]=i
        return res if(res!=len(nums)) else -1