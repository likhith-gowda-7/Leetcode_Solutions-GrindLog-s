class Solution:
    def binaryGap(self, n: int) -> int:
        binary=bin(n)[2:]
        if(binary.count("1")<2):
            return 0
        prev=100 if(binary[0]!="1") else 0
        res=0
        for i in range(1,len(binary)):
            if(binary[i]=="1"):
                diff=(i-prev)
                res=max(res,diff)
                prev=i
        return res
        
