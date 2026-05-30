class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        #There are only two choices in the operations,
        #1.Swap the even part and check
        #2.Swap the odd part and check
        res=[0,0]
        if((s1[0]==s2[0] and s1[2]==s2[2]) or (s1[0]==s2[2] and s1[2]==s2[0])):
            res[0]=1
        if((s1[1]==s2[1] and s1[3]==s2[3]) or (s1[1]==s2[3] and s1[3]==s2[1])):
            res[1]=1
        return sum(res)==2