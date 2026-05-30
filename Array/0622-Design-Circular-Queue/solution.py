class MyCircularQueue:

    def __init__(self, k: int):
        self.size=k
        self.queue=[None]*k
        self.front=0
        self.rear=-1

    def enQueue(self, value: int) -> bool:
        if(self.isFull()):
            return False
        self.rear=(self.rear+1)%self.size
        self.queue[self.rear]=value
        return True

    def deQueue(self) -> bool:
        if(self.isEmpty()):
            return False
        if(self.front==self.rear):
            self.front=0
            self.rear=-1
        else:
            self.front=(self.front+1)%self.size
        return True
    def Front(self) -> int:
        if(self.isEmpty()):
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if(self.isEmpty()):
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        if(self.rear==-1):
            return True
        else:
            return False

    def isFull(self) -> bool:
        if(not self.isEmpty() and (self.rear+1)%self.size==self.front):
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()