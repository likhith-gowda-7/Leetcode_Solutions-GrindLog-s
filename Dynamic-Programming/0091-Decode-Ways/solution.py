class Solution:
    def numDecodings(self, s: str) -> int:
        #Tablubation
        n=len(s)
        dp=[0]*n
        #this indicate the end(len(s)), meaning you can't take more and it makes a number
        dp.append(1)
        for i in range(n-1,-1,-1):
            #the digit shouldn't start as a 0
            if(s[i]!="0"):
                #option 1-> we can take a single digit as one number
                dp[i]+=dp[i+1]
                #OR
                #option 2-> we can take a two digit as one number, if it is <=26
                if(i+1<n and int(s[i:i+2])<=26):
                    dp[i]+=dp[i+2]
        return dp[0]
            