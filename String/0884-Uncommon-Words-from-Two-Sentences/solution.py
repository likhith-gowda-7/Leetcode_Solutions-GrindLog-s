class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        h1=defaultdict(int)
        curr=""
        for i in s1:
            if(i!=" "):
                curr+=i
            else:
                h1[curr]+=1
                curr=""
        h1[curr]+=1
        curr=""
        for i in s2:
            if(i!=" "):
                curr+=i
            else:
                h1[curr]+=1
                curr=""
        h1[curr]+=1
        res=[]
        for key,val in h1.items():
            if(val==1):
                res.append(key)
        return res
        