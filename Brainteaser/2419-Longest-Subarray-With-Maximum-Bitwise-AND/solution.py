class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxi=max(nums)
        max_value_count=0
        c=0
        for n in nums:
            if(n==maxi):
                c+=1
                max_value_count=max(c,max_value_count)
            elif(c!=0):
                c=0
        return max_value_count