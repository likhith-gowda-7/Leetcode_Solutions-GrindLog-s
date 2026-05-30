class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        if(len(nums)==len(set(nums))):
            return 0
        h1=defaultdict(list)
        count=0
        for ind,num in enumerate(nums):
            if(num in h1):
                for i in h1[num]:
                    if(ind*i%k==0):
                        count+=1
            h1[num].append(ind)
        return count

        