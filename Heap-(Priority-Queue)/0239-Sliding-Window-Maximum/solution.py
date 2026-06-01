class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if(len(nums)==1):
            return nums
        max_queue=deque()
        res=[]
        l=0
        for r in range(len(nums)):
            while max_queue and max_queue[-1]<nums[r]:
                max_queue.pop()
            max_queue.append(nums[r])
            if(r+1>=k):
                res.append(max_queue[0])
                if(nums[l]==max_queue[0]):
                    max_queue.popleft()
                l+=1
        return res