class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n=len(nums)//3
        left_sum=sum(nums[:n])
        max_heap=[-x for x in nums[:n]]
        heapq.heapify(max_heap)
        pre_arr=[0]*(2*n)
        pre_arr[n-1]=left_sum #index 1 we'll have left_sum
        for i in range(n,2*n):
            left_sum+=nums[i]
            left_sum-=-heapq.heappushpop(max_heap,-nums[i])
            pre_arr[i]=left_sum
        right_sum=sum(nums[2*n:])
        min_heap=nums[2*n:]
        heapq.heapify(min_heap)
        suf_arr=[0]*(2*n+1)
        suf_arr[2*n]=right_sum
        for i in range(2*n-1,n-1,-1):
            right_sum+=nums[i]
            right_sum-=heapq.heappushpop(min_heap,nums[i])
            suf_arr[i]=right_sum
        res=float("inf")
        for i in range(n-1,2*n):
            res=min(res,pre_arr[i]-suf_arr[i+1])
        return res
        
        