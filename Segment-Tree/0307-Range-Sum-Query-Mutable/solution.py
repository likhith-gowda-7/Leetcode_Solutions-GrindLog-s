class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.arr=nums    #we create a copy of know the old of that index
        self.BIT_Tree = [0] * (self.n + 1)
        for i,val in enumerate(nums):
            self.add(i,val)

    def add(self,ind,val):
        ind+=1
        while ind <= self.n:
            self.BIT_Tree[ind] +=val
            ind += ind & (-ind)     # for moving to its Next Resposible Index(NRI)

    def update(self, index: int, val: int) -> None:
        delta=val-self.arr[index] #this delta refers to the difference of value from previous value to curr value(that should be put in that index)
        self.arr[index]=val
        self.add(index,delta)

    def query(self, ind):
        ind += 1
        res = 0
        while ind > 0:
            res += self.BIT_Tree[ind]
            ind -= ind & (-ind)  # for moving to its parent
        return res

    def sumRange(self, left: int, right: int) -> int:
        return self.query(right) - self.query(left - 1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
