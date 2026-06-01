class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_map=defaultdict(int)
        prefix_map[0]=1
        curr_sum=0
        res=0
        for num in nums:
            curr_sum=(curr_sum+num)%k
            res+=prefix_map[curr_sum]
            prefix_map[curr_sum]+=1
        return res