class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        mini=len(nums)
        for i,val in enumerate(nums):
            if(val==target):
                mini=min(mini,abs(i-start))
        return mini

        