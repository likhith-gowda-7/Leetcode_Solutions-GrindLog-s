class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxi=0
        h1={0:-1}
        curr=0
        for i in range(len(nums)):
            if(nums[i]==1):
                curr+=1
            else:
                curr-=1
            if(curr in h1):
                maxi=max(maxi,(i-h1[curr]))
            else:
                h1[curr]=i
        return maxi

        


        