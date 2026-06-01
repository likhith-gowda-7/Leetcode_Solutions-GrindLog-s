class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.h1=Counter(nums1)
        #this map is to count the freq of a number
        self.h2=Counter(nums2)
        #this list to update the val at specific index(in hashmap we are storing count not index, so we need this)
        self.nums2=nums2

    def add(self, index: int, val: int) -> None:
        #decrease the count of old value
        self.h2[self.nums2[index]]-=1
        #increase the val in that index in nums2 list
        self.nums2[index]+=val
        #increase the count of that new_val
        new_val=self.nums2[index]
        self.h2[new_val]=self.h2.get(new_val,0)+1

    def count(self, tot: int) -> int:
        pairs=0
        for key,val in self.h1.items():
            find=tot-key
            if(find in self.h2):
                pairs+=self.h2[find]*val
        return pairs
# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)