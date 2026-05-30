class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls=0
        cows=0
        check=Counter(secret)
        used=set()
        for i in range(len(guess)):
            val=guess[i]
            if(val==secret[i]):
                bulls+=1
                check[val]-=1
                used.add(i)
        for i in range(len(guess)):
            val=guess[i]
            if(i not in used):
                if(val in check and check[val]>0):
                    cows+=1
                    check[val]-=1
        return str(bulls)+"A"+str(cows)+"B"
                
