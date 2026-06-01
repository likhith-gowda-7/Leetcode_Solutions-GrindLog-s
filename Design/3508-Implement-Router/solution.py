class Router:

    def __init__(self, memoryLimit: int):
        self.max_size=memoryLimit
        self.router=deque()
        self.packets=set()
        self.goal=defaultdict(deque)
        self.curr_size=0
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet=(source,destination,timestamp)
        if(packet in self.packets):
            return False
        if(self.curr_size==self.max_size):
            val=self.router.popleft()
            self.packets.remove(val)
            self.goal[val[1]].popleft()
            self.curr_size-=1
        #add the packet to the router
        self.router.append(packet)
        self.packets.add(packet)
        self.goal[destination].append(timestamp)
        self.curr_size+=1
        return True

    def forwardPacket(self) -> List[int]:
        if(self.curr_size==0):
            return []
        else:
            packet=self.router.popleft()
            self.packets.remove(packet)
            self.goal[packet[1]].popleft()
            self.curr_size-=1
            return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        time=self.goal[destination]
        if(not time):
            return 0
        left=bisect_left(time,startTime)
        right=bisect_right(time,endTime)
        return right-left

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)