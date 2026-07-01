class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        h1=defaultdict(lambda:-1)
        res=0
        for i,val in enumerate(s):
            h1[val]=i
            res+=1+min(h1['a'],h1['b'],h1['c'])
        return res

                