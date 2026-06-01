class SnapshotArray:
    def __init__(self, length: int):
        self.arr=defaultdict(list)
        self.call=0
    def set(self, index: int, val: int) -> None:
        if not self.arr[index] or self.arr[index][-1][0] != self.call:
            self.arr[index].append([self.call, val])
        else:
            self.arr[index][-1][1] = val  # Update latest value in the same snapshot
    def snap(self) -> int:
        self.call+=1
        return self.call-1
    def get(self, index: int, snap_id: int) -> int:
        value=self.arr.get(index,[])
        l=0
        r=len(value)-1
        while l<=r:
            mid=l+(r-l)//2
            if(value[mid][0]>snap_id):
                r=mid-1
            else:
                l=mid+1
        if(r>-1):
            return value[r][1]
        return 0



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)