class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums.sort()
        res=[]
        i=0
        curr=nums[0]
        while i<n:
            if(curr!=nums[i]):
                res.append(curr)
            else:
                i+=1
            curr+=1
        return res