class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n=len(bits)
        i=1
        one_bit=True
        while i<n:
            if(bits[i-1]==1):
                one_bit=False
                i+=2
            else:
                one_bit=True
                i+=1
        return i==n or one_bit