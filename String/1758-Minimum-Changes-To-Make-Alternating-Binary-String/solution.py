class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        ops=["0","1"]
        curr=1
        op1_cnt=0
        op2_cnt=0
        for i in range(n):
            if(s[i]!=ops[curr]):
                op1_cnt+=1
            else:
                op2_cnt+=1
            curr^=1
        return min(op1_cnt,op2_cnt)