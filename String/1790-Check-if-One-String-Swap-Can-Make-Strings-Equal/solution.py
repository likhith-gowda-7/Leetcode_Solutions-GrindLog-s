class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        h1=Counter(s1)
        if(s1==s2):
            return True
        count=0
        for i in range(len(s2)):
            if(s2[i] in h1 and h1[s2[i]]>0):
                if(s1[i]!=s2[i]):
                    count+=1
                h1[s2[i]]-=1
            else:
                return False
        if(count!=2):
            return False
        return True

            




       
        