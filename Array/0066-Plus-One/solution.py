class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        Change=False
        for i in range(len(digits)-1,-1,-1):
            if(digits[i]!=9):
                digits[i]+=1
                Change=True
                break
            else:
                digits[i]=0
        if(not Change):
            digits.insert(0,1)
        return digits
        