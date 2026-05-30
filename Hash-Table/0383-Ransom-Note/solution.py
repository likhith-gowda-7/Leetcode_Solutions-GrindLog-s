class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h=defaultdict(int)
        for s in magazine:
            h[s]+=1
        j=0
        for i in ransomNote:
            if(i in h):
                if(h[i]>0):
                    h[i]-=1
                    j+=1
        return j==len(ransomNote)


        