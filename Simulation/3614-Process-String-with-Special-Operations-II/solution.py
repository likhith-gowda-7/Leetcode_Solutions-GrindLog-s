class Solution:
    def processStr(self, s: str, k: int) -> str:
        Length=0
        for ch in s:
            if(ord(ch)>96):
                Length+=1
            elif(ch=="#"):
                Length*=2
            elif(ch=="*" and Length>0):
                Length-=1
        if(k>=Length):
            return "."
        for ch in reversed(s):
            if(ch=="#"):
                Length//=2
                if(k>=Length):
                    k-=Length
            elif(ch=="*"):
                Length+=1
            elif(ch=="%"):
                k=(Length-k)-1
            else:
                Length-=1
            if(Length==k):
                return ch
        return "."