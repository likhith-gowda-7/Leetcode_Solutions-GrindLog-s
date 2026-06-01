class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        curr_sum=nums1[0]+nums2[0]
        # sum,nums1_idx,nums2_idx
        heap=[(curr_sum,0,0)]
        res=[]
        n1_length=len(nums1)
        n2_length=len(nums2)
        check=set()
        while k>0 and heap:
            s,i,j=heappop(heap)
            if((i,j) in check):
                continue
            res.append((nums1[i],nums2[j]))
            check.add((i,j))
            #two options:
            #option 1
            if((i+1)<n1_length):
                heappush(heap,(nums1[i+1]+nums2[j],i+1,j))
            if((j+1)<n2_length):
                heappush(heap,(nums1[i]+nums2[j+1],i,j+1))
            k-=1
        return res