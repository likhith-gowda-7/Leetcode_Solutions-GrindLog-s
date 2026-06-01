class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r=deque()
        d=deque()
        l=len(senate)
        for i in range(l):
            if(senate[i]=="R"):
                r.append(i)
            else:
                d.append(i)
        while r and d:
            if(r[0]<d[0]):
                r.append(r.popleft()+l)
                d.popleft()
            else:
                d.append(d.popleft()+l)
                r.popleft()
        if(r):
            return "Radiant"
        return "Dire"