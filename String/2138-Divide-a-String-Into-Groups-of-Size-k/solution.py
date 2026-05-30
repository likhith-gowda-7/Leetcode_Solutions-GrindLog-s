class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res=[]
        c=0
        val=""
        for ch in s:
            c+=1
            val+=ch
            if(c==k):
                res.append(val)
                c=0
                val=""
        if(c!=0 and c<k):
            while c<k:
                c+=1
                val+=fill
            res.append(val)
        return res
        
