class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxi=0
        l=0
        uni=set()
        curr=0
        for r in range(len(nums)):
            val=nums[r]
            curr+=val
            while val in uni:
                n=nums[l]
                uni.remove(n)
                curr-=n
                l+=1
            maxi=max(maxi,curr)
            uni.add(val)
        return maxi
            