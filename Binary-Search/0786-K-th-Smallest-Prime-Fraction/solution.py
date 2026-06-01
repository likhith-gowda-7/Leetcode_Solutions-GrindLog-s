class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        min_heap=[]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                fraction=-(arr[i]/arr[j])
                if(len(min_heap)<k):
                    heapq.heappush(min_heap,(fraction,[arr[i],arr[j]]))
                else:
                    if(fraction>min_heap[0][0]):
                        heapq.heappushpop(min_heap,(fraction,[arr[i],arr[j]]))
        return min_heap[0][1]
        