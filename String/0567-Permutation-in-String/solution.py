class Solution(object):
    def checkInclusion(self, s1, s2):
        le=len(s1)
        c1=[0]*26
        c2=[0]*26
        if(len(s1)>len(s2)):
            return False
        for i in range(le):
            c1[ord(s1[i])-97]+=1
            c2[ord(s2[i])-97]+=1
        if(c1==c2):
            return True
        l=0
        for r in range(le,len(s2)):
            c2[ord(s2[r])-97]+=1
            c2[ord(s2[l])-97]-=1
            if(c1==c2):
                return True
            l+=1
        return False
        