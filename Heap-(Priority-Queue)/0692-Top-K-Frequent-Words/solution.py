class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        h1=Counter(words)
        h1=dict(sorted(h1.items()))
        maxi=max(h1.values())
        freq=[[] for _ in range(maxi+1)]
        res=[]
        for key,val in h1.items():
            freq[val].append(key)
        length=0
        for i in range(maxi,-1,-1):
            for s in freq[i]:
                res.append(s)
                length+=1
                if(length==k):
                    return res

        
        