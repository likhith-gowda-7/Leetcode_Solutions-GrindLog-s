class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        #if n is already a power of 2, then return True
        if(bin(n).count("1")==1):
            return True
        def check(x):
            return "".join(sorted(str(x)))
        target=check(n)
        l=len(target)
        till=pow(10,l)
        for i in range(1,30):
            p=pow(2,i)
            if(p>=till):
                break
            curr=check(p)
            if(curr==target):
                return True
        return False