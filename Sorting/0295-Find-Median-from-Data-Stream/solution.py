class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]

    def addNum(self, num: int) -> None:
        #here we do half spilting in clever way
        if(len(self.small)==len(self.large)):
            #here we first add to the small and then max(top) ele and add to large
            val=heapq.heappushpop(self.small,-num)
            heapq.heappush(self.large,-val)
        #this tells that large heap has more elements so take min(top) from it and append it to small heap
        else:
            val=heapq.heappushpop(self.large,num)
            heapq.heappush(self.small,-val)

    def findMedian(self) -> float:
        #if both are equal that means its even so find average
        if(len(self.small)==len(self.large)):
            return (-self.small[0]+self.large[0])/2
        #if not then return the top ele of large heap
        return self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()