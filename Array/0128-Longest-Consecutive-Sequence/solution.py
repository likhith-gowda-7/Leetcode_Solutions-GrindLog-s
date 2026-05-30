class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        maxi=0
        for num in nums:
            if((num-1) not in nums):
                prev=num
                count=1
                while prev+1 in nums:
                    prev+=1
                    count+=1
                if(count>maxi):
                    maxi=count
        return maxi
        