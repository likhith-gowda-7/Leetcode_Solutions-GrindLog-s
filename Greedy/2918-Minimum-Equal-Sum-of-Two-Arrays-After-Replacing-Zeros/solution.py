class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_sum=sum(nums1)
        nums2_sum=sum(nums2)
        nums1_zeros=nums1.count(0)
        nums2_zeros=nums2.count(0)
        #after adding 1 in place of 0
        nums1_sum+=(nums1_zeros*1)
        nums2_sum+=(nums2_zeros*1)
        if(nums1_sum<=nums2_sum and nums1_zeros>0 or nums1_sum==nums2_sum):
            return nums2_sum
        elif(nums2_sum<nums1_sum and nums2_zeros>0):
            return nums1_sum
        return -1

        