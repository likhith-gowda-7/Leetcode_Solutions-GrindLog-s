class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev,nex=0,0
        for i in range(len(flowerbed)):
            if(flowerbed[i]==0):
                if(i>0):
                    prev=flowerbed[i-1]
                if(i<len(flowerbed)-1):
                    nex=flowerbed[i+1]
                if(prev==0 and nex==0 and n>0):
                    flowerbed[i]=1
                    n-=1
                    if(n==0):
                        return True
        return n==0

                
                
       
                
       