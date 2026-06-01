class LFUCache:
    #here we are using the OrderedDict instead of LinkeList
    def __init__(self, capacity: int):
        self.cap=capacity
        self.lfucnt=0
        #key to count map
        self.cntmap=defaultdict(int)
        #count to element in OrderedDict map
        self.freqmap=defaultdict(OrderedDict)

    def Counter(self,key):
        cnt=self.cntmap[key]
        self.cntmap[key]+=1
        val=self.freqmap[cnt].pop(key,None)
        #if the current count key has no more elements than pop it from dict 
        if(not self.freqmap[cnt]):
            self.freqmap.pop(cnt)
            if(cnt==self.lfucnt):
                self.lfucnt+=1
        #after that, add this key to the new count's dict
        self.freqmap[cnt+1][key]=val
        return val
        
    def get(self, key: int) -> int:
        if(key not in self.cntmap):
            return -1
        val=self.Counter(key)
        #return value of that key from freqmap
        return val

    def put(self, key: int, value: int) -> None:
        #if the below condition just change the value of key and increase its lfu count
        if(key in self.cntmap):
            self.freqmap[self.cntmap[key]][key]=value
            self.Counter(key)
            return
        #this is for removing the Least Frequently Used (LFU) element
        if(key not in self.cntmap and len(self.cntmap)==self.cap):
            res=self.freqmap[self.lfucnt].popitem(last=False)
            self.cntmap.pop(res[0])
        #this part of code executes when you add new element
        self.cntmap[key]=1
        self.freqmap[1][key]=value
        #the lfu will be 1 bcoz it says new element is added, so there is a Least Frequently Used (LFU) element's count that can be used to remove element
        self.lfucnt=1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)