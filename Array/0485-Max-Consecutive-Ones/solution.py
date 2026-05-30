class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        curr=0
        for n in nums:
            if(n):
                curr+=1
            else:
                maxi=max(maxi,curr)
                curr=0
        maxi=max(maxi,curr)
        return maxi