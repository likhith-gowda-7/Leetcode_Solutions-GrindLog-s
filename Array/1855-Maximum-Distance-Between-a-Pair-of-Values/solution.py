class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i=0
        j=0
        n1=len(nums1)
        n2=len(nums2)
        res=0
        while i<n1 and j<n2:
            if(i>j):
                j+=1
                continue
            if(nums1[i]<=nums2[j]):
                j+=1
                res=max(res,j-i)
            else:
                i+=1
        return res-1 if(res) else 0

        