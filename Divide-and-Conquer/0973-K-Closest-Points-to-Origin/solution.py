class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for i in range(len(points)):
            x,y=points[i]
            distance=-((x*x)+(y*y))
            if(len(heap)==k):
                if(heap[0][0]<distance):
                    heapq.heappushpop(heap,(distance,points[i]))
            else:
                heapq.heappush(heap,(distance,points[i]))
        res=[]
        for _,val in heap:
            res.append(val)
        return res