class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        for n in arr:
            diff=-abs(n-x)
            if(len(heap)<k):
                heapq.heappush(heap,(diff,n))
            else:
                if(heap[0][0]<diff):
                    heapq.heappop(heap)
                    heapq.heappush(heap,(diff,n))
        
        res=[]
        for diff,n in heap:
            res.append(n)
        return sorted(res)