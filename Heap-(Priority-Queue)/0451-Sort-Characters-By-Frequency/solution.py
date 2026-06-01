class Solution:
    def frequencySort(self, s: str) -> str:
        h1=Counter(s)
        heap=[]
        for key,val in h1.items():
            heapq.heappush(heap,(-val,key))
        res=""
        while heap:
            val,key=heapq.heappop(heap)
            res+=key*(-val)
        return res
        


        