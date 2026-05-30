class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i]
        heapq.heapify(stones)
        while len(stones)>1:
            stone1=heapq.heappop(stones)
            stone2=heapq.heappop(stones)
            diff=(-stone1)-(-stone2)
            if(diff):
                heapq.heappush(stones,-diff)
        return -stones[0] if(stones) else 0