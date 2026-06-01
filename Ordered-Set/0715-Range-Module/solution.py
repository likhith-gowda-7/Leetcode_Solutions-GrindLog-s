class RangeModule:

    def __init__(self):
        self.interval=[]

    def addRange(self, left: int, right: int) -> None:
        bisect.insort(self.interval,[left,right])
        res=[self.interval[0]]
        for i in range(1,len(self.interval)):
            intv=self.interval[i]
            if(res[-1][1]>=intv[0]):
                res[-1][1]=max(intv[1],res[-1][1])
            else:
                res.append(intv)
        self.interval=res

    def queryRange(self, left: int, right: int) -> bool:
        ind=bisect.bisect(self.interval,[left,int(1e9)])
        if(ind==0):
            return False
        return self.interval[ind-1][1]>=right

    def removeRange(self, left: int, right: int) -> None:
        res=[]
        for intv in self.interval:
            #this means the whole range(interval) should be removed
            if(left<=intv[0] and right>=intv[1]):
                continue
            elif(left>=intv[1] or right<=intv[0]):
                res.append(intv)
            elif(left<intv[0]):
                res.append([right,intv[1]])
            elif(right>intv[1]):
                res.append([intv[0],left])
            else:
                res.append([intv[0],left])
                res.append([right,intv[1]])
        self.interval=res   

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)