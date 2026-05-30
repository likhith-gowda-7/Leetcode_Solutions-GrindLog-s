class Solution:
    def countPoints(self, rings: str) -> int:
        h1=defaultdict(set)
        for i in range(0,len(rings),2):
            col=rings[i]
            rod=rings[i+1]
            h1[rod].add(col)
        count=0
        for c in h1.values():
            if(len(c)==3):
                count+=1
        return count


        