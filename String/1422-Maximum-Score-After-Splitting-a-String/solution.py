class Solution:
    def maxScore(self, s: str) -> int:
        left=0
        right=s.count("1")
        maxi=0
        for i in range(1,len(s)):
            if(s[i-1]=="0"):
                left+=1
            else:
                right-=1
            if(left+right>maxi):
                maxi=left+right
        return maxi



        