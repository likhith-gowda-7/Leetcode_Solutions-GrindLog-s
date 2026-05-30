class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n=len(rains)
        lakes_to_day=defaultdict(list)
        res=[-1]*n
        #here we list the lake and it's raining day
        for i,lake in enumerate(rains):
            if(lake>0):
                lakes_to_day[lake].append(i)
        #this is track all the filled lakes
        full_lakes=set()
        #heap helps us to get the next flooding lake 
        min_heap=[]
        for day in range(n):
            lake=rains[day]
            if(lake>0):
                if(lake in full_lakes):
                    return []
                full_lakes.add(lake)
                lakes_to_day[lake].pop(0)
                if(lakes_to_day[lake]):
                    heappush(min_heap,(lakes_to_day[lake][0],lake))
            else:
                if(min_heap):
                    next_day,next_flood_lake=heappop(min_heap)
                    full_lakes.remove(next_flood_lake)
                    res[day]=next_flood_lake
                else:
                    res[day]=1
        return res

            
                