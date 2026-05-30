class Solution:
    def countTriples(self, n: int) -> int:
        squares=set()
        for i in range(1,n+1):
            squares.add(pow(i,2))
        res=0
        for val1 in squares:
            for val2 in squares:
                if(val1!=val2):
                    s=val1+val2
                    if(s in squares):
                        res+=1
        return res
