class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n=len(nums)
        maxi=max(nums)
        freq=[[0,-c] for c in range(maxi+1)]
        result=[]
        k-=1
        for i in range(n):
            freq[nums[i]][0]-=1 
            if(i>=k):
                heap=freq.copy()
                curr=0
                heapify(heap)
                j=0
                while j<x and heap[0][0]!=0:
                    count,num=heappop(heap)
                    curr+=(-count)*(-num)
                    j+=1
                result.append(curr)
                freq[nums[i-k]][0]+=1
        return result