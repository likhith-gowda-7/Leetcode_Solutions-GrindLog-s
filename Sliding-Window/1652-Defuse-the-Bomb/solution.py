class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if(k==0):
            return [0]*len(code)
        res=[0]*len(code)
        start=1
        end=k
        if(k<0):
            start=len(code)-abs(k)
            end=len(code)-1
        window=0
        for i in range(start,end+1):
            window+=code[i]
        for i in range(len(code)):
            res[i]=window
            window-=code[start%len(code)]
            window+=code[(end+1)%len(code)]
            start+=1
            end+=1
        return res

        