class Solution:
    def numSteps(self, s: str) -> int:
        steps=0
        carry=0
        for i in range(len(s)-1,0,-1):
            curr_bit=int(s[i])
            if(curr_bit ^ carry):
                steps+=2
                carry=1
            else:
                steps+=1
        return steps+carry