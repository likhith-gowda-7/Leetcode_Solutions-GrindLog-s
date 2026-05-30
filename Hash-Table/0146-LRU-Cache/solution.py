class LRUCache:
#here we are using OrderedDict instead of Doubly Linked List
    def __init__(self, capacity: int):
        self.cap=capacity
        self.length=0
        #OrderedDict consisting key-value pairs
        self.valmap=OrderedDict()

    def get(self, key: int) -> int:
        if(key not in self.valmap):
            return -1
        self.valmap.move_to_end(key)
        return self.valmap[key]

    def put(self, key: int, value: int) -> None:
        if(key in self.valmap):
            self.valmap[key]=value
            self.valmap.move_to_end(key)
            return
        if(self.length==self.cap):
            self.valmap.popitem(last=False)
            self.length-=1
        self.valmap[key]=value
        self.length+=1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)