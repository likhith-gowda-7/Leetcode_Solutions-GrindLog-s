class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr=nums[:]
        if(nums):
            heapq.heapify(self.arr)
            while len(self.arr)>k:
                heapq.heappop(self.arr)
        self.k=k

    def add(self, val: int) -> int:
        if(len(self.arr)<self.k):
            heapq.heappush(self.arr,val)
        else:
            if(val>self.arr[0]):
                heapq.heappushpop(self.arr,val)
        return self.arr[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)