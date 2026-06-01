class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def find(r,arr):
            l=0
            while l<=r:
                mid=(l+r)//2
                if(arr[mid]>=0):
                    l=mid+1
                else:
                    r=mid-1
            return l
        neg=0
        for arr in grid:
            size=len(arr)
            neg+=(size-find(size-1,arr))
        return neg