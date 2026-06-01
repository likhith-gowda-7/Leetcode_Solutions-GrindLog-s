class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        idx=0
        i=0
        l=len(nums)
        res=[]
        near_key_idx=None
        while i<l:
            if(nums[i]==key):
                while idx<l:
                    diff=abs(i-idx)
                    if(nums[idx]==key):
                        near_key_idx=idx
                    if(diff<=k):
                        res.append(idx)
                    elif(diff>k and idx>i):
                        break
                    idx+=1
            if(near_key_idx!=None and near_key_idx>i):
                i=near_key_idx
            elif(idx>i):
                i=idx
            else:
                i+=1
        return res