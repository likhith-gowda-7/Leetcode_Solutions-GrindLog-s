class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ch={0:1}
        prefix_sum=0
        res=0
        for num in nums:
            prefix_sum+=num
            if(prefix_sum-goal in ch):
                res+=ch[prefix_sum-goal]
            if(prefix_sum in ch):
                ch[prefix_sum]+=1
            else:
                ch[prefix_sum]=1
        return res

        