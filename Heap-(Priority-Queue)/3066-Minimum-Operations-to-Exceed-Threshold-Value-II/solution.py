class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        minheap=[]
        for n in nums:
            heapq.heappush(minheap,n)
        curr=0
        op=0
        while minheap:
            min1=heapq.heappop(minheap)
            if(min1>=k):
                break
            min2=heapq.heappop(minheap)
            curr=min1*2+min2
            heapq.heappush(minheap,curr)
            op+=1
        return op

