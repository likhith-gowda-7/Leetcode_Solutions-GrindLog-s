class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum=curr=sum(nums[:k])
        for i in range(k,len(nums)):
            curr+=nums[i]-nums[i-k]
            max_sum=max(max_sum,curr)
        return max_sum/k
        
        
