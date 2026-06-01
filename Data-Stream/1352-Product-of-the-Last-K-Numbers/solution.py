class ProductOfNumbers:

    def __init__(self):
        self.prefix=[1]
        self.l=1
        self.zero=0
    def add(self, num: int) -> None:
        last=self.prefix[-1]
        if(last==0):
            self.zero=len(self.prefix)-1
            self.prefix.append(num)
        else:
            self.prefix.append(last*num)
        self.l+=1
    def getProduct(self, k: int) -> int:
        if(self.zero>=self.l-k):
            return 0
        if(self.prefix[self.l-k-1]==0):
            return self.prefix[-1]
        else:
            return self.prefix[-1]//self.prefix[len(self.prefix)-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)