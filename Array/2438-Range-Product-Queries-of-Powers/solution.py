class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod=pow(10,9)+7
        binary=bin(n)[2:]
        powers=[]
        for i,val in enumerate(reversed(binary)):
            if(val=="1"):
                if(not powers):
                    powers.append(pow(2,i))
                else:
                    prev=powers[-1]
                    powers.append(prev*pow(2,i))
        #prefix sum
        res=[]
        for start,end in queries:
            curr=powers[end]
            if(start!=0):
                curr//=powers[start-1]
            curr%=mod
            res.append(curr)
        return res