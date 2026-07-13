class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq="123456789"
        res=[]
        for i in range(10):
            for j in range(i+1,10):
                num=int(seq[i:j])
                if(low<=num<=high):
                    res.append(num)
                elif(num>high):
                    break
        res.sort()
        return res
