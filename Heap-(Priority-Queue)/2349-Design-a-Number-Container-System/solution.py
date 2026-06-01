class NumberContainers:

    def __init__(self):
        self.h1=defaultdict(SortedSet)
        self.h2=defaultdict(int)
    def change(self, index: int, number: int) -> None:
        if(index in self.h2):
            num=self.h2[index]
            self.h1[num].remove(index)
        self.h1[number].add(index)
        self.h2[index]=number
    def find(self, number: int) -> int:
        if(self.h1[number]):
            mini=self.h1[number]
            return mini[0]
        else:
            return -1
# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)