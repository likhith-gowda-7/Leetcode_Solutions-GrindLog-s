class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        s=set("aeiou")
        rang=[0]*len(words)
        prev=0
        for i,w in enumerate(words):
            if(w[0] in s and w[-1] in s):
                prev+=1
            rang[i]=prev
        res=[0]*len(queries)
        for i,q in enumerate(queries):
            l,r=q
            if(l==0):
                res[i]=rang[r]
            else:
                res[i]=rang[r]-rang[l-1]
        return res



        