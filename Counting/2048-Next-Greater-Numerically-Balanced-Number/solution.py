class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def find(num):
            count=[0]*10
            while num:
                last=num%10
                count[last]+=1
                num=num//10
            for i in range(1,10):
                if(count[i]>0 and i!=count[i]):
                    return False
            return True if(count[0]==0) else False
        for digit in range(n+1,int(1e7)):
            if(find(digit)):
                return digit
        

