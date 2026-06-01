class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        res=[]
        h1=defaultdict(int)
        for i,j in items1+items2:
            h1[i]+=j
        for key,val in h1.items():
            res.append([key,val])
        return sorted(res)
        