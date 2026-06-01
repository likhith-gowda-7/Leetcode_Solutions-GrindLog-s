class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        res=float("-inf")
        maxi=deque()
        for r in range(len(nums)):
            nums[r]+=nums[maxi[0]] if maxi else 0
            res=max(res,nums[r])
            while maxi and nums[maxi[-1]]<nums[r]:
                maxi.pop()
            if(nums[r]>0):
                maxi.append(r)
            if(maxi and maxi[0]==r-k):
                maxi.popleft()
        return res