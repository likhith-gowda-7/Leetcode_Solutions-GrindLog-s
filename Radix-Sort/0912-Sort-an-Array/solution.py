class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        new_arr=[]
        heapq.heapify(nums)
        while nums:
            new_arr.append(heapq.heappop(nums))
        return new_arr