class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        count=0
        h1=defaultdict(int)
        h2=defaultdict(int)
        res=[]
        for pos,col in queries:
            if(pos in h1):
                h2[h1[pos]]-=1
                if(h2[h1[pos]]==0):
                    del h2[h1[pos]]
            h1[pos]=col
            h2[col]+=1
            res.append(len(h2))
        return res
