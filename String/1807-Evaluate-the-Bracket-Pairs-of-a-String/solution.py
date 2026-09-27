class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        h1=defaultdict(str)
        for key,val in knowledge:
            h1[key]=val
        res=""
        curr=""
        found=False
        for ch in s:
            if(ord(ch)<97):
                if(ch=="("):
                    found=True
                else:
                    res+=h1[curr] if(h1[curr]!="") else "?"
                    curr=""
                    found=False
            else:
                if(found):
                    curr+=ch
                else:
                    res+=ch
        return res