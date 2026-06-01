class LUPrefix:

    def __init__(self, n: int):
        self.arr=[False]*n
        self.ind_count=0
        self.n=n

    def upload(self, video: int) -> None:
        self.arr[video-1]=True
        while self.ind_count<self.n and self.arr[self.ind_count]:
            self.ind_count+=1

    def longest(self) -> int:
        return self.ind_count


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()