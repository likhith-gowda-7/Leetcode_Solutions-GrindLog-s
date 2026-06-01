class Solution:
    def clearStars(self, s: str) -> str:
        pos=0
        n=len(s)
        h1=defaultdict(deque)
        while pos<n:
            if(s[pos]!="*"):
                h1[s[pos]].append(pos)
            else:
                mini=min(h1.keys())
                h1[mini].pop()
                if(not h1[mini]):
                    del h1[mini]
            pos+=1
        res=""
        for i in range(n):
            if(h1[s[i]] and h1[s[i]][0]==i):
                res+=s[i]
                h1[s[i]].popleft()
        return res