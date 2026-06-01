class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        maxi=deque([0])
        le=len(nums)
        res=nums[0]
        for r in range(1,le):
            res=nums[maxi[0]]+nums[r]
            nums[r]=res
            while maxi and nums[maxi[-1]]<nums[r]:
                maxi.pop()
            maxi.append(r)
            if(maxi[0]<r-k+1):
                maxi.popleft()
        return res
            