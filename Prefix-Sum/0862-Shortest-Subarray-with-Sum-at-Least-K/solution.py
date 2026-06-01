class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        curr=0
        dq=deque()
        res=float('inf')
        for j in range(len(nums)):
            curr+=nums[j]
            if(curr>=k):
                res=min(res,j+1)
            while dq and curr-dq[0][1]>=k:
                l=dq[0][0]
                dq.popleft()
                res=min(res,j-l)
            while dq and curr<dq[-1][1]:
                dq.pop()
            dq.append([j,curr])
        if(res==float('inf')):
            return -1
        return res
        