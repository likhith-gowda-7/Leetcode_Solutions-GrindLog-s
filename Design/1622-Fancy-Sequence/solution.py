class Fancy:

    def __init__(self):
        self.nums=[]
        self.adds=0
        self.multi=1
        self.mod=pow(10,9)+7
    def power(self, a, b):
        res = 1
        a %= self.mod
        while b > 0:
            if b & 1:
                res = (res * a) % self.mod
            a = (a * a) % self.mod
            b >>= 1
        return res

    def append(self, val: int) -> None:
        x=((val-self.adds)%self.mod+self.mod)*self.power(self.multi,self.mod-2)%self.mod
        self.nums.append(x)

    def addAll(self, inc: int) -> None:
        self.adds=(self.adds+inc)%self.mod

    def multAll(self, m: int) -> None:
        self.adds=(self.adds*m)%self.mod
        self.multi=(self.multi*m)%self.mod
    def getIndex(self, idx: int) -> int:
        if(idx>=len(self.nums)):
            return -1
        curr=((self.nums[idx]*self.multi)+self.adds)%self.mod
        return curr

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)