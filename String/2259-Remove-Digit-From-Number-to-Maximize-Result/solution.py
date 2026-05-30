class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxi=""
        for i in range(len(number)):
            temp=""
            if(number[i]==digit):
                temp=number[:i]+number[i+1:]
            if(temp>maxi):
                maxi=temp
        return maxi

       
        
                


        