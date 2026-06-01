class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        h1=Counter(nums)
        pairs=0
        for key,val in h1.items():
            if(key>=k):
                diff=key-k
                if(diff in h1):
                    pairs+=h1[diff]*val
        return pairs