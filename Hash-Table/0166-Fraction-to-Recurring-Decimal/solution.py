class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        if(n==0 or d==0):
            return "0"
        minus=False
        if(n<0 and d<0):
            minus=False
        elif(n<0 or d<0):
            n=abs(n)
            d=abs(d)
            minus=True
        remainder_map={}
        res=""
        if(minus):
            res+="-"
        dot=False
        while True:
            div=n//d
            remain=n%d
            res+=str(div)
            if(remain==0 or remain in remainder_map):
                break
            if(not dot):
                dot=True
                res+="."
            remainder_map[remain]=len(res)
            n=remain*10
        remain=n%d
        if(remain not in remainder_map):
            return res
        idx=remainder_map[remain]
        res=list(res)
        res.append(")")
        res.insert(idx,"(")
        return "".join(res)
        
        
