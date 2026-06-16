class Solution:
    def processStr(self, s: str) -> str:
        ans=""
        for ch in s:
            if(ord(ch)>96):
                ans+=ch
            elif(ans):
                if(ch=="*"):
                    ans=ans[:-1]
                elif(ch=="#"):
                    ans+=ans
                elif(ch=="%"):
                    ans=ans[::-1]
        return ans