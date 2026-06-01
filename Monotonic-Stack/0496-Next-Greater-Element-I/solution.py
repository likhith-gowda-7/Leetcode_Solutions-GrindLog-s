class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        h=defaultdict(int)
        for i in nums2:
            while stack and stack[-1]<i:
                val=stack.pop()
                h[val]=i
            stack.append(i)
        for i in range(len(nums1)):
            if(nums1[i] not in h):
                nums1[i]=-1
            else:
                nums1[i]=h[nums1[i]]
        return nums1
