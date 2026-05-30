class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums=sorted(list(set(nums)))
        count=0
        mini=nums[0]
        for i in range(1,len(nums)):
            diff=nums[i]-mini
            if(diff>k):
                count+=1
                mini=nums[i]
        return count+1
        